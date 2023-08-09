import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')  # captura una linea
    header = next(reader)  # obtiene encabezado
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value
                      for key, value in iterable}  # construye diccionario
      data.append(country_dict)  # dicionario a lista
    return data


if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])
