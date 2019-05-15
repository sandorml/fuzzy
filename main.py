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
        'NoColor & NoEsNumero & EstaMedio'        
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
        'NoColor': pi(0, 1, 2, 3),
        'EsColor': pi(4, 5, 6, 7),
        'NoEsNumero': pi(0, 1, 4, 5),
        'NoSeguroDeNumero': pi(4, 5, 6, 7),
        'ConozcoNumero': pi(6, 7, 9, 10),
        'EstaCerca': pi(0, 1, 4, 5),
        'EstaMedio': pi(2, 3, 4, 5),
        'EstaLejos': pi(4.5, 5, 6.5, 8),
        'Caliente': triangular(1, 2, 3),
        'Normal': triangular(2.5, 3.5, 4),
        'Frio': triangular(3.8, 5, 6),
        'Rapido': pi(6.5, 8, 9, 10),
        'Medio': pi(4.5, 5, 6, 7.5),
        'Lento': triangular(0, 5, 3)
    }

    m = Mamdani(rules, implications, memb, (0, 10))
    val = m.evaluate({
        'EsColor': 6,
        'NoColor': 6,

        'ConozcoNumero': 9,
        'NoSeguroDeNumero': 9,
        'NoEsNumero': 9,

        'EstaCerca': 6,
        'EstaLejos': 6,
        'EstaMedio': 6,

        'Caliente': 3,
        'Normal': 3,
        'Frio': 3

    })
    x, y = m.implications(val)

    print(m.defuzzification(x, y, 'b'))

    pl.plot(x, y)

    pl.show()

# velocidad promedio
# 5km/h caminando
# 6km/h trotando
# 10km/h corriendo

if __name__ == "__main__":
    guaguas()

