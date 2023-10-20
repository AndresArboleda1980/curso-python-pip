import random
epsilon = 0.01

def generar_centroides(k):
    """Genera k puntos al azar

    Parámetros:
    k int > 0

    Retorna: Lista de k listas de puntos x,y [[int, int], [int, int],...]
    """
    centroids = []
    count = 1
    for _ in range(k):
        if count == 5:
            count = 1

        x = random.randint(0, 5) #Genera puntos con coordenadas de -10 a 10
        y = random.randint(0, 5)        
        if count == 1:
            x = x
            y = y
        elif count == 2:
            x = -x
        elif count == 3:
            x = -x
            y = -y
        elif count == 4:
            y = -y

        centroid = [x, y]
        centroids.append(centroid)
        count += 1

    print(f'Centroides originales: {centroids}')
    return centroids
    

def clusterizar(puntos, centroides):
    """Calcula la distancia de una lista de puntos designados por coordenas x,y con
    una lista de centroides con coordenadas x,y.

    Parámetros:
    puntos list [[int, int], [int, int],...]
    centroides list [[int, int], [int, int],...]

    Retorna: Lista con listas con punto, centroide_asignado, distancia_punto_centroide 
    [[[int, int], [int, int], float], [[int, int], [int, int], float], ...]
    """
    elementos_clusters = []    

    for punto in puntos:
        puntos_centroides_distancias = []
        for centroide in centroides:
            distancia_calculada = distancia(punto, centroide)
            puntos_centroides_distancias.append(distancia_calculada)
        # print(f'len: {len(puntos_centroides_distancias)}')
        # print(puntos_centroides_distancias)
        # print('\n')

        distancias_calculadas = []
        for el in puntos_centroides_distancias:
            distancias_calculadas.append(el[2])
        # print(f'Distancias punto-centroides: {distancias_calculadas}')        

        distancia_min = min(distancias_calculadas)
        # print(f'Distancia min: {distancia_min}')
        
        for el in puntos_centroides_distancias:
            if el[2] == distancia_min:
                elementos_clusters.append(el)
                break  
    
    print(f'Elementos: {elementos_clusters}')
    print(f'Cantidad elementos: {len(elementos_clusters)}')
    print('\n')
    return elementos_clusters


def distancia(punto_1, punto_2):
    """Cálcula la distancia euclidiana entre dos puntos.
    
    Parámetros:
    punto_1, punto_2 list [int, int]
    
    Retorna:
    Una lista con el punto_1, punto_2 y su distancia calculada
    [[int, int], [float, float], float]
    """
    a = punto_1[0]
    b = punto_1[1]
    c = punto_2[0]
    d = punto_2[1]

    result = ((a - c)**2 + (b - d)**2)**0.5 #Cálculo de distancia euclidiana

    return [punto_1, punto_2, result]


def calcular_nuevos_centroides(elementos_cluster, centroids):
    """Calcula el punto promedio de una serie de puntos relacionados para
    convertirlo en el nuevo centroide del cluster.

    Parámetros:
    elementos_cluster list [[punto, centroide, distancia], [punto, centroide, distancia], ...]
    k int > 0

    Retorna:
    Lista con los nuevos centroides calculados en forma [x, y]
    list [centroide, centroide, ...]
    Sumas de distancias de centroide con sus puntos
    list [suma_de_distancias, suma_de_distancias, ...]
    """
    new_centroids = []
    sumas_distancias = []
    for centroid in centroids:
        print(f'Centroid: {centroid}')
        puntos_centroide = []
        for el in elementos_cluster:
            if el[1] == centroid:
                puntos_centroide.append(el)
        print(f'Puntos del cluster: {puntos_centroide}')        

        x_coord = []
        y_coord = []
        suma_de_distancias = 0        
        for el in puntos_centroide:
            x_coord.append(el[0][0])
            y_coord.append(el[0][1])
            suma_de_distancias += el[2]    
        new_x = sum(x_coord) / len(puntos_centroide)
        new_y = sum(y_coord) / len(puntos_centroide)   
        print(f'Suma distancias puntos a centroide: {suma_de_distancias}')  
        print(f'New centroid: x {new_x}, y {new_y}')
        print('\n')

        sumas_distancias.append(suma_de_distancias)
        new_centroid = [new_x, new_y]
        new_centroids.append(new_centroid)
    
    print(f'New centroids: {new_centroids}')
    return (new_centroids, sumas_distancias)
    

def agrupamiento_k_means(vectors, k):
    diferencia_sumas_distancias = 100
    total_distancias = 100

    centroides = generar_centroides(k)

    while diferencia_sumas_distancias > epsilon:
        elementos = clusterizar(vectors, centroides)
        nuevos_centroides, sumas_distancias = calcular_nuevos_centroides(elementos, centroides)
        diferencia_sumas_distancias = total_distancias - sum(sumas_distancias)
        total_distancias = sum(sumas_distancias)
        centroides = nuevos_centroides    

        print(f'Total suma distancias puntos-centroide: {total_distancias}')
        print('---'*15 + '\n')        


if __name__ == "__main__":
    coordenadas = [[2, 1], [3, 5], [4, 5], [-1, 2], [-3, 3], [-3, 1], [-1, -4], [-2, -2], [-2, -1], [3, -4], [4, -5], [4, -3]]
    agrupamiento_k_means(coordenadas, 4)