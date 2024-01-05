import pandas as pd
import random
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os

# Configuración para Qt en modo offscreen para evitar el error
os.environ['QT_QPA_PLATFORM'] = 'offscreen'

# Crear un DataFrame de ejemplo (reemplaza esto con tu archivo CSV real)
n = 100  # Número de registros aleatorios
random_data = pd.DataFrame({
    'Fecha': pd.date_range(start='2022-01-01', periods=n),
    'Magnitud': [round(random.uniform(2, 8), 1) for _ in range(n)]
})

# Crear una tabla HTML a partir del DataFrame
html_table = random_data.to_html(classes='table table-bordered table-hover', index=False)

# Generar una gráfica de barras a partir de los datos
plt.figure(figsize=(10, 6))
plt.bar(random_data['Fecha'], random_data['Magnitud'], width=5, color='dodgerblue')
plt.xlabel('Fecha')
plt.ylabel('Magnitud')
plt.title('Gráfica de Barras de Magnitud de Terremotos')
plt.grid(True)

# Guardar la gráfica en un archivo
plt.savefig('grafica_de_barras.png')

# Convertir la gráfica en una representación en base64
buffer = BytesIO()
plt.savefig(buffer, format='png')
image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

# Crear el contenido HTML
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Tabla y Gráfica de Barras</title>
</head>
<body>
    <h1>Tabla de Datos</h1>
    {html_table}
    <h1>Gráfica de Barras</h1>
    <img src="data:image/png;base64, {image_base64}" alt="Gráfica de Barras">
</body>
</html>
"""

# Guardar el contenido HTML en un archivo
with open('tabla_y_grafica.html', 'w') as f:
    f.write(html_content)

# Mostrar la tabla HTML
print("Tabla HTML generada:")
print(html_table)

# Mostrar la gráfica
plt.show()

print("Gráfica de barras guardada en 'grafica_de_barras.png'")
print("Archivo HTML generado: 'tabla_y_grafica.html'")