from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.transform import linear_cmap
from bokeh.palettes import Spectral11
import numpy as np

# Datos de ejemplo
n = 100  # Número de burbujas
x = np.random.random(size=n) * 10  # Coordenadas x aleatorias
y = np.random.random(size=n) * 10  # Coordenadas y aleatorias
size = np.random.random(size=n) * 2  # Tamaños aleatorios de burbujas
colors = [Spectral11[i % 11] for i in range(n)]  # Colores de burbujas

# Crear una fuente de datos
source = ColumnDataSource(data=dict(x=x, y=y, size=size, colors=colors))

# Crear un mapeo de colores
mapper = linear_cmap(field_name='size', palette=Spectral11, low=min(size), high=max(size))

# Crear la figura
p = figure(title="Bubble Chart Example", x_axis_label="X-axis", y_axis_label="Y-axis", width=800, height=400)

# Agregar las burbujas al gráfico
p.circle(x='x', y='y', size='size', source=source, color=mapper, legend_field='size')

# Generar el gráfico como un archivo HTML
output_file("bubble_chart22.html")

# Mostrar el gráfico
show(p)
