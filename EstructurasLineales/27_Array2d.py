import numpy as np

class Matriz2D:
    def __init__(self, filas, columnas):
        self.matriz = np.zeros((filas, columnas))

    def asignar_valor(self, fila, columna, valor):
        self.matriz[fila][columna] = valor

    def obtener_valor(self, fila, columna):
        return self.matriz[fila][columna]

    def sumar_matrices(self, otra_matriz):
        if self.matriz.shape == otra_matriz.matriz.shape:
            resultado = Matriz2D(self.matriz.shape[0], self.matriz.shape[1])
            resultado.matriz = self.matriz + otra_matriz.matriz
            return resultado
        else:
            return None

    def recorrer_matriz(self, funcion):
        filas, columnas = self.matriz.shape
        for i in range(filas):
            for j in range(columnas):
                funcion(self.matriz[i][j])

    def __str__(self):
        return str(self.matriz)

# Crear una matriz 2x2
matriz1 = Matriz2D(2, 2)

# Asignar valores a la matriz
matriz1.asignar_valor(0, 0, 1)
matriz1.asignar_valor(0, 1, 2)
matriz1.asignar_valor(1, 0, 3)
matriz1.asignar_valor(1, 1, 4)

# Imprimir las matrices
print("Matriz 1:")
print(matriz1)

# Crear una función para imprimir cada elemento
def imprimir_elemento(elemento):
    print(f"Elemento: {elemento}")

# Recorrer la matriz y aplicar la función
print("Recorriendo la matriz:")
matriz1.recorrer_matriz(imprimir_elemento)
