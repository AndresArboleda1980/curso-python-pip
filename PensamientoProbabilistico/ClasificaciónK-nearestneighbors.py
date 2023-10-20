import math
from bokeh.io import output_notebook, show
from bokeh.plotting import figure

def welcome():
    print('Welcome to the K-Nearest neighbors code implementation')
    print(f'{"+"*54}')
    
    calidad = int(input("Ingrese la calidad del producto en una escala de 1 a 10: "))
    precio = int(input("Ingrese el precio del producto en una escala de 1 a 10: "))
    k = int(input('Ingrese el número de vecinos que desea comparar (Impar menor de 6): '))

    print(f'El precio ingresado:{precio} con calidad:{calidad}')

    return calidad, precio, k

def graficar(DATOS,calidad,precio):
    x_values = []
    y_values = []

    p = figure(title='Relacion precio calidad', x_axis_label='Calidad', y_axis_label='Precio')

    for key in DATOS:
        x_values.append(key[0])
        y_values.append(key[1])

    p.circle(x_values, y_values, size=15, line_color="navy", fill_color="red", fill_alpha=0.5,legend_label="Datos Clasificados",)
    p.circle(calidad, precio, size=15, line_color="navy", fill_color="blue", fill_alpha=0.5,legend_label="Dato usuario",)

    show(p)

def vecinos(DATOS,distancias,k,keys):

    indices_vecino_mas_cercanos = []
    contador_costoso = 0
    contador_calidad = 0

    #Ordena la lista para conocer las distancias cortas
    distancias_ordenadas = list(sorted(distancias))

    #Unicamente evalua los vecinos que el usuario desea comparar, encontrando a que par de coordenadas corresponen las distancias pequeñas
    for i in range(k):
        value = distancias_ordenadas[i]
        indices_vecino_mas_cercanos.append(distancias.index(value))

    #Recorre los pares coordenados que están más cerca para ver si son costosos y calidosos
    for i in indices_vecino_mas_cercanos:
        tag = keys[i]
        
        print(f'Vecino cercano: {tag} ')

        if DATOS[tag] == 'costoso':
            contador_costoso += 1
        else:
            contador_calidad += 1
    
    if contador_calidad > contador_costoso:
        print('Su producto es calidoso')
    elif contador_calidad < contador_costoso:
        print('Su producto es costoso')
    else:
        print('Su producto no pudo ser calificado')

def calculo_distancia(DATOS,calidad,precio):

    distancias = []
    keys = []

    for key in DATOS:
        tuples = (key[0]),(key[1])
        keys.append(tuples)

        distancia = math.sqrt((calidad - key[0])**2 + (precio - key[1])**2)
        distancias.append(distancia)
        
    return distancias ,keys

if __name__ == "__main__":
    #Pide al usuario su opinión sobre el precio y la calidad del producto a evaluar, también el número de vecinos con que desea comparar.
    calidad, precio, k = welcome()

    DATOS = {
        (2,5) : 'costoso',
        (1,4) : 'costoso',
        (2,6) : 'costoso',
        (5,1) : 'calidad',
        (6,3) : 'calidad',
        (4,1) : 'calidad',
    }

    #Calcula las distancias con respecto a todos los puntos, devuelve arreglo de distantancias y arreglo con las coordenas de los productos ya clasificados
    distancias, keys = calculo_distancia(DATOS,calidad,precio)
    vecinos(DATOS,distancias,k,keys)
    graficar(DATOS,calidad,precio)