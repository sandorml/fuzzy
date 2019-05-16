from aggregation_methods import Mamdani, Larsen
from membership_function import pi, triangular
import matplotlib.pyplot as pl
import sys


def guaguas(color=5, numero=8, distancia=4, agregation_meth='m', membership_func='c'):
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
        'NoColor': pi(0, 2, 4, 6),
        'EsColor': pi(3, 5, 7, 10),
        'NoEsNumero': pi(0, 1, 4, 5),
        'NoSeguroDeNumero': pi(4, 5, 6, 7),
        'ConozcoNumero': pi(6, 7, 9, 10),
        'EstaCerca': pi(0, 1, 2.5, 3),
        'EstaMedio': pi(2.8, 3.5, 5, 6),
        'EstaLejos': pi(5.5, 6, 9, 10),
        'Caliente': triangular(1, 2, 3),
        'Normal': triangular(2.5, 3.5, 4),
        'Frio': triangular(3.8, 5, 6),
        'Rapido': pi(7, 8, 9, 10),
        'Medio': pi(4.5, 6, 6.5, 7.5),
        'Lento': pi(1, 2.5, 3, 5)
    }

    m = Mamdani(rules, implications, memb, (0, 10)) if agregation_meth == 'm' else Larsen(
        rules, implications, memb, (0, 10))
    val = m.evaluate({
        'EsColor': color,
        'NoColor': color,

        'ConozcoNumero': numero,
        'NoSeguroDeNumero': numero,
        'NoEsNumero': numero,

        'EstaCerca': distancia,
        'EstaLejos': distancia,
        'EstaMedio': distancia

    })
    x, y = m.implications(val)

    print(membership_func)
    print(m.defuzzification(x, y, membership_func))

    pl.plot(x, y)

    pl.show()

# velocidad promedio
# 5km/h caminando
# 6km/h trotando
# 10km/h corriendo


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        guaguas(
            color=int(sys.argv[1]),
            numero=int(sys.argv[2]),
            distancia=int(sys.argv[3]),
            agregation_meth=sys.argv[4],
            membership_func= sys.argv[5]
        )
    else:
        print('Introduce los parámetros')
