import folium
import pandas as pd
import random

# Crear un objeto de mapa con Folium
m = folium.Map(location=[0, 0], zoom_start=2)

# Cargar datos de terremotos (por ejemplo, desde un archivo CSV)
terremotos = pd.read_csv("data_terremotos.csv")

# Seleccionar una población aleatoria de 500 registros
sampled_terremotos = random.sample(terremotos.index.tolist(), 500)

# Iterar a través de los datos de terremotos y agregar marcadores al mapa
for index in sampled_terremotos:
    row = terremotos.iloc[index]
    folium.Marker([row["Latitude"], row["Longitude"]], tooltip=row["OrigID"]).add_to(m)

# Guardar el mapa en un archivo HTML
m.save("mapa_terremotos1212.html")
