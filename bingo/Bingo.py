import itertools
import openpyxl
import random

def generar_tarjetas_bingo(n):
    # Definir rangos para cada columna
    columnas = {
        'B': list(range(1, 16)),
        'I': list(range(16, 31)),
        'N': list(range(31, 46)),
        'G': list(range(46, 61)),
        'O': list(range(61, 76))
    }

    # Generar todas las posibles combinaciones de números
    combinaciones = list(itertools.product(*columnas.values()))

    # Elegir N combinaciones aleatorias si N es menor que el número total de combinaciones
    if n < len(combinaciones):
        combinaciones = random.sample(combinaciones, n)

    # Organizar las combinaciones en una matriz
    matriz_tarjetas = [list(comb) for comb in combinaciones]

    return matriz_tarjetas

def guardar_en_excel(matriz_tarjetas, nombre_archivo):
    # Crear un nuevo libro de Excel
    libro = openpyxl.Workbook()

    # Crear pestañas para cada letra
    letras = ['B', 'I', 'N', 'G', 'O']
    for letra in letras:
        hoja = libro.create_sheet(title=letra)

        # Escribir las tarjetas en la hoja de Excel
        for i, tarjeta in enumerate(matriz_tarjetas, start=1):
            hoja.append([f'Tarjeta {i}'] + [f'{letra}{valor}' for valor in tarjeta])

    # Eliminar la hoja por defecto
    default_sheet = libro.get_sheet_by_name('Sheet')
    libro.remove_sheet(default_sheet)

    # Guardar el libro de Excel
    libro.save(nombre_archivo)

if __name__ == "__main__":
    # Especificar el número de tarjetas a generar
    N = 500

    # Generar las tarjetas
    tarjetas = generar_tarjetas_bingo(N)

    # Guardar las tarjetas en un archivo Excel
    guardar_en_excel(tarjetas, 'tarjetas_bingo.xlsx')
