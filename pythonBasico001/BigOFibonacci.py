# O(1) Constante
# O(n) Lineal
# O(Log n) Logaritmica
# O(n Log n) Logaritmica Natural
# O(n**2) polinomial
# O(2**n) Exponencial
# recursividad múltiple

def fibonacci(n):
    
    if n ==  or n == 1:
        return 1

     return   fibonacci (n - 1) + fibonacci (n - 2)

#Big o simplifica en este caso de la recursividad en su crecimiento en O(2**n).
# se da en función de las veces que se llame la función fibonacci
# O(2**n)      