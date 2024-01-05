import folium
from folium.plugins import HeatMap
import random

# Crear un objeto de mapa con Folium
m = folium.Map(location=[0, 0], zoom_start=2)

# Generar datos aleatorios para ubicaciones
n = 100  # Número de puntos aleatorios
data = []
for _ in range(n):
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    data.append([lat, lon])

# Agregar un mapa de calor a las ubicaciones aleatorias
HeatMap(data).add_to(m)

# Guardar el mapa de calor en un archivo HTML
m.save("mapa_de_calor.html")