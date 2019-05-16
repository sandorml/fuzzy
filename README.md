# 				 									Informe 

## 								Proyecto de simulacíon Lógica difusa


​							 **Sándor Martín Leyva C-412**



### Características del Sistema de Inferencia Propuesto

El sistema propuesto consta de funciones de pertenencia `triangulares` y `trapezoidales`. También posee los métodos de agregación de `Mamdani` y `Larsen` al igual que todos los métodos de desdifusificación (`Centroide`, `Bisección` y todas las variantes de los `Máximos`)

### Principales Ideas seguidas para la implementación del Sistema

Para la implementación se utilizó `python` por la facilidad que brinda para resolver problemas numéricos librerías como `numpy` y el trabajo con funciones.

Las reglas se definen como un `string` su estructura sería
```
 'A & B | C'
```
y su consecuencia sería otro `string`, estos se guardan en listas independientes
```
rules = [
    'A & B | C',
    'A | B | C'
]

consequent = [
    'X',
    'Z'
]
```

donde el consecuente de la primera regla seria `consequent[0]`.

Las funciones de membresía se le asignan a cada variable de una regla en forma de diccionario, aqui tenemos la facilidad de utilizar currying en dichas funciones con el objetivo de pasarle los parámetros de las funciones pero seguir esperando por la `x` (*el valor del dominio donde se va a evluar la función*)
```python
from membership_function import pi, triangular

membership_func = {
    'A': pi(0, 2, 4, 6),
    'B': pi(1, 3, 4, 7),
    'C': triangular(0, 2, 1),
    'X': pi(3, 3.6, 4, 6),
    'Z': pi(0, 2, 4, 6),
}
```

Para utilizar los `métodos de agregación` solo hay que llamarlos y pasarle los parámetros requeridos

```python
from aggregation_methods import Mamdani, Larsen
domain = (0,10)
m = Mamdani(rules, consequent, membership_func, domain)
l = Larsen(rules, consequent, membership_func, domain)
```

Los `métodos de agregación` tienen la funcion `evaluate` que recibe un diccionario con los valores que se van a utilizar para inferir una respuesta a partir de las reglas definidas

```python
m.evaluate({
    A: 5
    B: 6
    C: 1
})
```

este va a devolver todas las reglas con sus variables evaluadas, listas para pasar por el proceso de evaluación de la regla y poder calcular el valor consecuente para luego pasar por el proceso de desdifusiﬁcación


### Propuesta de Problema a Solucionar mediante inferencia difusa
Dado al evidente problema del transporte en nuestra ciudad, el ciudadano que tiene que tomar los ómnibus para desplazarse de un lugar a otro pasa mucho trabajo, muchas veces dicho ómnibus no para en los lugares reglamentados y hay que correr hasta este, pero no siempre estamos seguros si correr o no, ya que no estamos seguros de que es el número que necesitamos o es del color designado para esa ruta o puede que estemos muy lejos y no valga la pena dar la carrera. Para la solución de este problema se va a emplear `Lógica Difusa`, para saber a que velocidad debemos desplazarnos hacia el ómnibus en caso de que tengamos interes en cogerlo.

*Para la solción de este problema hay que tener e cuenta las velocidades promedios de una persona al caminar, trotar y correr*

**Velocidad promedio**
​    
     1-5 km/h caminando
     6-7 km/h trotando
     8-10 km/h corriendo

### Consideraciones obtenidas a partir de la solución del problema con el sistema de inferencia implementado
No hay consideraciones. Los resultados obtenidos del sistema varian en dependencia del los métodos de agregación o de las funciones de pertenencia utilizadas, pero no significa que unos esten bien o mal, solo son distintos puntos de vista.


**Ejecutar el proyecto:**

Para la ejecución del sistema de inferencia es necesario tener `numpy` y `matplotlib` instalados

```
python main.py <seguridad de que es el color del ómnibus > <seguridad de que es el color del ómnibus > <distancia> <método de agregación> <función de membresía>
```
    <seguridad de que es el color del ómnibus > (1,10) 
    <seguridad de que es el color del ómnibus > (1,10)
    <distancia> (1,10) sería de 1-100 metros pero los valores se dividen entre 10
    <método de agregación> {
                                m -> Mamdani
                                l -> Larsen
                            } 
    <función de membresía> {  
                                c -> centroide
                                b -> bisección
                                mc -> máximo central
                                mp -> máximo más pequeño
                                mg -> máximo más grande
                            }





