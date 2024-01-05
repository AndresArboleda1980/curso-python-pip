import pandas as pd
import folium
import random

# Crear un DataFrame de ejemplo (reemplaza esto con tu archivo CSV real)
n = 100  # Número de registros aleatorios
random_data = pd.DataFrame({
    'Latitude': [random.uniform(-90, 90) for _ in range(n)],
    'Longitude': [random.uniform(-180, 180) for _ in range(n)],
    'Magnitud': [random.uniform(0, 9) for _ in range(n)],
     'Magnitud': [random.uniform(0, 9) for _ in range(n)]
})

# Crear un mapa de Folium
m = folium.Map(location=[0, 0], zoom_start=2)

# Agregar círculos de colores en función de la magnitud
for i in range(n):
    lat = random_data.iloc[i]['Latitude']
    lon = random_data.iloc[i]['Longitude']
    mag = random_data.iloc[i]['Magnitud']

    if mag < 2:
        color = 'green'
    elif mag < 4:
        color = 'yellow'
    else:
        color = 'red'

    folium.CircleMarker(
        location=[lat, lon],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        popup=f'Magnitud: {mag}'
    ).add_to(m)

# Guardar el mapa en un archivo HTML
m.save("mapa_coropletico11.html")
