import folium

# Crear un objeto de mapa con Folium
m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# Agregar marcadores al mapa
folium.Marker([51.5074, -0.1278], tooltip="Londres").add_to(m)
folium.Marker([48.8566, 2.3522], tooltip="París").add_to(m)
folium.Marker([40.7128, -74.0060], tooltip="Nueva York").add_to(m)
folium.Marker([4.7128, -4.0060], tooltip="Nueva York").add_to(m)

# Guardar el mapa en un archivo HTML
m.save("GraficaDeMapas55.html")