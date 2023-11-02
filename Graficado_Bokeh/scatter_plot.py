from bokeh.plotting import figure, show, output_file

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Crear un objeto figura
p = figure(title="Scatter Plot Example", tools="pan,box_zoom,reset,save")

# Dibujar los puntos en el scatter plot
p.scatter(x, y, size=10, color="blue", alpha=0.5)

# Guardar el gráfico en un archivo HTML
output_file("scatter_plot2.html")

# Mostrar el gráfico en una ventana del navegador
#show(p)