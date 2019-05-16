from rules import Rule
import numpy as np

def middle_index(i: int, l: list, old_l=float('-inf'), old_r=float('inf')):
    rigth = sum([l[idx] for idx in range(i, len(l))])
    left = sum(l) - rigth
    if rigth == left or abs(old_l-old_r) < abs(left-rigth) or i+1 >= len(l) or i-1 < 0:
        if abs(old_l-old_r) < abs(left-rigth):
            return i, old_l, old_r
        return i, left, rigth
    elif rigth > left:
        return middle_index(i+1, l, left, rigth)
    return middle_index(i-1, l, left, rigth)


class AggregationMethods:
    def __init__(self, consequent):
        self.consequent = consequent

    def implications(self, results: list):
        print(results)
        return self.consequent(self, results)

    def defuzzification(self, x: list, y: list, type='c'):
        '''
        type:   
                c -> centroide
                b -> biseccion
                mc -> maximo central
                mp -> maximo mas pequenno
                mg -> maximo mas grande
        '''
        if type == 'b':
            return AggregationMethods.biseccion(x, y)
        elif type == 'mc':
            return AggregationMethods.middle_of_maximum(x, y)
        elif type == 'mp':
            return AggregationMethods.smallest_of_maximum(x, y)
        elif type == 'mg':
            return AggregationMethods.largest_of_maximum(x, y)
        return AggregationMethods.centroide(x, y)

    @staticmethod
    def centroide(x: list, y: list):
        num = 0
        den = 0
        for i in range(len(x)):
            num += x[i]*y[i]
            den += y[i]
        return num/den

    @staticmethod
    def biseccion(x: list, y: list):
        result, _, _ = middle_index(int(len(y)/2), y)
        return x[result]

    @staticmethod
    def middle_of_maximum(x: list, y: list):
        max_l = max(y)
        values = []
        for i in range(len(y)):
            if y[i] == max_l:
                values.append(x[i])
        return np.average(values)

    @staticmethod
    def smallest_of_maximum(x: list, y: list):
        return x[y.index(max(y))]

    @staticmethod
    def largest_of_maximum(x: list, y: list):
        y.reverse()
        x.reverse()
        return AggregationMethods.smallest_of_maximum(x, y)


class Mamdani(AggregationMethods):
    def __init__(self, rules: list, implications: list, membership_function: dict, domain: tuple):
        self.implication = implications
        self.membership_function = membership_function
        self.domain = domain

        AggregationMethods.__init__(self, Mamdani.consequent_filter)
        self.rules = [Rule(item.split(), max, min, lambda x: 1-x)
                      for item in rules]

    def evaluate(self, values: dict):
        result = []
        for item in self.rules:
            val = item.evaluate({k: self.membership_function[k](
            v) for k, v in values.items()})
            result.append(val)
        return result

    @staticmethod
    def consequent_filter(self, results):
        values_x = []
        values_y = []
        for i in range(len(results)):
            implication = self.implication[i]
           
            for x in np.arange(self.domain[0], self.domain[1], 0.01):
                y = self.membership_function[implication](x)
               
                vy = y if results[i] >= y and y >= 0 else results[i]
                
                if not x in values_x:
                    values_x.append(x)
                    values_y.append(vy)
                else:
                    i_x = values_x.index(x)
                    values_y[i_x] = values_y[i_x] if values_y[i_x] > vy else vy
        
        return values_x, values_y


class Larsen(Mamdani):
    def __init__(self, rules: list, implications: list, membership_function: dict, domain: tuple):
        Mamdani.__init__(self, rules, implications,
                         membership_function, domain)
        AggregationMethods.__init__(self, Larsen.consequent_filter)

    @staticmethod
    def consequent_filter(self, results):
        values_x = []
        values_y = []
        for i in range(len(results)):
            implication = self.implication[i]
            for x in np.arange(self.domain[0], self.domain[1], 0.01):
                y = self.membership_function[implication](x)
                vy = y*results[i]
                if not x in values_x:
                    values_x.append(x)
                    values_y.append(vy)
                else:
                    i_x = values_x.index(x)
                    values_y[i_x] = values_y[i_x] if values_y[i_x] > vy else vy
        return values_x, values_y
