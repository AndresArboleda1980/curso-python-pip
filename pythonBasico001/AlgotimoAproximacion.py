objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001 #  esto nos indica que tan precisos queremos ser.
paso = epsilon**2 # esto define que tanto nos acercamos en cada iteración
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:#nos proteje de los valores nulos
    #print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')