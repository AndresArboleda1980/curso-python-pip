'''
Clases de complejidad algorítmica
Existen distintos tipos de complejidad algorítmica:

### Algotimos que son recomendados para cualquier tipo de computo

O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.

###los algoitmos que crecen de forma  Log lineal de capacida de computo media

O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.

###los algoritmos que crecen de forma Polinomial, Exponencial y Factorial 
  No deben ser usados para volumesnes altos de información

O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.
'''

# O(1) Constante
# O(n) Lineal
# O(Log n) Logaritmica
# O(n Log n) Logaritmica Natural
# O(n**2) polinomial
# O(2**n) Exponencial

def f(n):
    for i in range(n):

        for j in range(n):
            print(i,j)
#BIG_O en este caso simplifica a una ecuanción cuadratica por ser un loop dentro de un loop siempre
#el caso que fuera un solo loop seria lineal
#  O(n) * O(n) = O(n * n) = O(n**2) 

