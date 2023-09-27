import numpy as np

class Matriz3D:
    def __init__(self, dimensiones):
        self.matriz = np.zeros(dimensiones)

    def asignar_valor(self, x, y, z, valor):
        self.matriz[x][y][z] = valor

    def obtener_valor(self, x, y, z):
        return self.matriz[x][y][z]

    def suma_total(self):
        return np.sum(self.matriz)

    def promedio_total(self):
        return np.mean(self.matriz)

# Crear una matriz tridimensional de dimensiones 3x3x3
dimensiones = (3, 3, 3)
matriz_3d = Matriz3D(dimensiones)

# Asignar valores a la matriz
for x in range(3):
    for y in range(3):
        for z in range(3):
            matriz_3d.asignar_valor(x, y, z, x + y + z)

# Obtener y mostrar el valor en una posición específica
x = 1
y = 2
z = 0
valor = matriz_3d.obtener_valor(x, y, z)
print(f"Valor en la posición ({x}, {y}, {z}): {valor}")

# Calcular la suma total y el promedio total de la matriz
suma_total = matriz_3d.suma_total()
promedio_total = matriz_3d.promedio_total()

print(f"Suma total de la matriz: {suma_total}")
print(f"Promedio total de la matriz: {promedio_total}")
