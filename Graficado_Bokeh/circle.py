from bokeh.plotting import figure, output_file, show

# Crear datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Crear una figura de Bokeh
p = figure(title="Gráfico de Dispersión Simple", x_axis_label="X-axis", y_axis_label="Y-axis")

# Agregar puntos a la figura
p.circle(x, y, size=10, color="navy", alpha=0.5)

# Especificar el archivo de salida (HTML)
output_file("scatter.html")

# Mostrar la figura en un navegador web
show(p)
