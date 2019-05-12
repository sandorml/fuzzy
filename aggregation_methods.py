from rules import Rule
import numpy as np


class AggregationMethods:
    def __init__(self, implications: list, membership_function: dict, x: tuple):
        self.membership_function = membership_function
        self.implication = implications
        self.x = x

    #TODO: hay que hacerla union de todos las listas de las x y las y
    def implications(self, results: list):
        values_x = []
        values_y = []
        for i in range(len(results)):
            values__x = []
            values__y = []
            implication = self.implication[i]
            for x in np.arange(self.x[0], self.x[1], 0.01):
                y = self.membership_function[implication](x)
                if results[i] >= y and y >= 0:
                    values__x.append(x)
                    values__y.append(y)
                else:
                    values__x.append(x)
                    values__y.append(results[i])
            values_x.append(values__x)
            values_y.append(values__y)
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
        if type=='b':
            return self.biseccion(x,y)         
        elif type=='mc':
            return self.middle_of_maximum(x,y)
        elif type=='mp':
            return self.smallest_of_maximum(x,y)
        elif type=='mg':
            return self.largest_of_maximum(x,y)
        
        return self.centroide(x,y)

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
    def  middle_of_maximum(x: list, y: list):
        max_l = max(y)
        values = []
        for i in range(len(y)):
            if y[i] == max_l:
                values.append(i)
        return np.average(values)

    @staticmethod
    def  smallest_of_maximum(x: list, y: list):
        return x[y.index(max(y))]

    @staticmethod
    def  largest_of_maximum(x: list, y: list):
        y.reverse()
        return self.smallest_of_maximum(x,y)
    


class Mamdani(AggregationMeth):
    def __init__(self, rules: list, implications: list, membership_function: dict, x: tuple):
        AggregationMeth.__init__(self, implications, membership_function, x)
        self.rules = [Rule(item.split(), max, min) for item in rules]

    def evaluate(self, values: dict):
        result = [item.evaluate({k: self.membership_function[k](
            v) for k, v in values.items()}) for item in self.rules]
        return result
