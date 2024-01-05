from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Select
from bokeh.layouts import column
import pandas as pd

# Cargar los datos desde el archivo CSV
data = pd.read_csv('data_terremotos.csv')

# Crear una fuente de datos ColumnDataSource
source = ColumnDataSource(data)

# Crear la figura principal
plot = figure(width=800, height=400, title="Storytelling: Terremotos")
plot.circle('Longitude', 'Latitude', source=source, size=8, color='red', alpha=0.6)

# Agregar herramienta de información al pasar el mouse
hover = HoverTool()
hover.tooltips = [("Fecha", "@Date"), ("Magnitud", "@Magnitud")]
plot.add_tools(hover)

# Crear elementos interactivos para la historia
select_magnitud = Select(title="Filtrar por Magnitud", options=['Todos'] + [str(m) for m in data['Magnitud'].unique()])

# Función para actualizar los datos al cambiar la selección
def update_data(attrname, old, new):
    selected_magnitud = select_magnitud.value
    if selected_magnitud == 'Todos':
        new_data = data
    else:
        new_data = data[data['Magnitud'] == float(selected_magnitud)]

    source.data = ColumnDataSource.from_df(new_data)

select_magnitud.on_change('value', update_data)

# Crear el archivo HTML de salida
output_file("storytelling_terremotos.html")

# Crear el diseño de la historia
layout = column(select_magnitud, plot)

# Mostrar la historia
show(layout)
