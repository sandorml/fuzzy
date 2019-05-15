from aggregation_methods import Mamdani, Larsen
from membership_function import pi, triangular
import matplotlib.pyplot as pl
import sys


def guaguas():
    rules = [
        'EsColor & ConozcoNumero & EstaCerca',
        'EsColor & ConozcoNumero & EstaLejos',
        'EsColor & ConozcoNumero & EstaMedio',
        
        'EsColor & NoSeguroDeNumero & EstaCerca',
        'EsColor & NoSeguroDeNumero & EstaLejos',
        'EsColor & NoSeguroDeNumero & EstaMedio',

        'EsColor & NoEsNumero & EstaCerca',
        'EsColor & NoEsNumero & EstaLejos',
        'EsColor & NoEsNumero & EstaMedio',

        'NoColor & ConozcoNumero & EstaCerca',
        'NoColor & ConozcoNumero & EstaLejos',
        'NoColor & ConozcoNumero & EstaMedio',
        
        'NoColor & NoSeguroDeNumero & EstaCerca',
        'NoColor & NoSeguroDeNumero & EstaLejos',
        'NoColor & NoSeguroDeNumero & EstaMedio',

        'NoColor & NoEsNumero & EstaCerca',
        'NoColor & NoEsNumero & EstaLejos',
        'NoColor & NoEsNumero & EstaMedio',

        
    ]


    implications = [
        'Lento',
        'Rapido',
        'Medio',

        'Lento',
        'Rapido',
        'Medio',

        'Lento',
        'Lento',
        'Lento',

        'Lento',
        'Rapido',
        'Medio',
        
        'Medio',
        'Medio',
        'Medio',

        'Lento',
        'Lento',
        'Lento'
    ]

    memb = {
        'EsColor': pi(0, 1, 2, 3),
        'NoColor': pi(4, 5, 6, 7),
        'ConozcoNumero': pi(0, 1, 4, 5),
        'NoSeguroDeNumero': pi(4, 5, 6, 7),
        'NoEsNumero': pi(6, 7, 9, 10),
        'EstaCerca': pi(0, 1, 4, 5),
        'EstaMedio': pi(2, 3, 4, 5),
        'EstaLejos': pi(4, 5, 6, 7),
        'Caliente': triangular(1, 2, 3),
        'Normal': triangular(2.5, 3.5, 4),
        'Frio': triangular(3.8, 5, 6),
        'Rapido': pi(0, 3, 5, 6),
        'Medio': pi(0, 6, 8, 9),
        'Lento': triangular(8.5, 9, 10)
    }

    m = Mamdani(rules, implications, memb, (0, 10))
    val = m.evaluate({
        'EsColor': 5,
        'NoColor': 5,

        'ConozcoNumero': 4,
        'NoSeguroDeNumero': 4,
        'NoEsNumero': 4,

        'EstaCerca': 3,
        'EstaLejos': 3,
        'EstaMedio': 3,

        'Caliente': 3,
        'Normal': 3,
        'Frio': 3

    })
    x, y = m.implications(val)

    print(m.defuzzification(x, y, 'b'))

    pl.plot(x, y)

    pl.show()


if __name__ == "__main__":
    guaguas()

