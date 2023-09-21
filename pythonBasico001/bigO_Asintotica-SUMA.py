'''
Clases de complejidad algorítmica
Existen distintos tipos de complejidad algorítmica:

O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
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

# Ley de la suma

def f(n)
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

#Para la simplificación en BIG_O complejidad asintotica no se tiene en cuenta 
#las constantes en este caso el numero el numero 2
#  O(n) + O(n) = O(n + n) = O(2n) = O(n)

#############################################################
#SEGUNDO CASO
#############################################################
# Ley de la suma

def f(n)
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)
#BIG_O en este caso simplifica el termino de menos peso en esta caso n**1
#  O(n) + O(n * n) = O(n**1 + n**2) = O(n**2) 