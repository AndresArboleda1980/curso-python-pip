objetivo = int(input('Escoge un numero: '))
epsilon = 0.001 #  esto nos indica que tan precisos queremos ser.
bajo = 0.0 # limite inferior
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}',abs(respuesta**2 - objetivo))
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')