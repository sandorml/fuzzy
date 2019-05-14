from rules import Rule
import numpy as np


class AggregationMethods:
    def __init__(self, implications: list, membership_function: dict, domain: tuple):
        self.membership_function = membership_function
        self.implication = implications
        self.domain = domain

    def implications(self, results: list):
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
        pass

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
        AggregationMethods.__init__(
            self, implications, membership_function, domain)
        self.rules = [Rule(item.split(), max, min) for item in rules]

    def evaluate(self, values: dict):
        result = [item.evaluate({k: self.membership_function[k](
            v) for k, v in values.items()}) for item in self.rules]
        return result
