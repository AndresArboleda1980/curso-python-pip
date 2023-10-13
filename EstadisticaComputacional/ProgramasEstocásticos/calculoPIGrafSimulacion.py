import os
import random
import math
import statistics
from bokeh.plotting import figure, output_file, show

os.system('cls')

tries = 10
puntos = 100

def estimar_pi(puntos):
    in_circle_x = []
    in_circle_y = []
    out_circle_x = []
    out_circle_y = []

    for i in range(puntos):
        pos_x = random.uniform(-1, 1)
        pos_y = random.uniform(-1, 1)

        if math.sqrt(pos_x**2 + pos_y**2) <= 1:
            in_circle_x.append(pos_x)
            in_circle_y.append(pos_y)
        else:
            out_circle_x.append(pos_x)
            out_circle_y.append(pos_y)

    estimate_pi = (4 * len(in_circle_x)) / puntos
    return (estimate_pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y)

def crear_muestra(tries):
    pi_array = []
    in_circle_x = []
    in_circle_y = []
    out_circle_x = []
    out_circle_y = []

    for i in range(tries):
        pivalor, in_x, in_y, out_x, out_y = estimar_pi(puntos)
        pi_array.append(pivalor)
        in_circle_x.extend(in_x)
        in_circle_y.extend(in_y)
        out_circle_x.extend(out_x)
        out_circle_y.extend(out_y)

    return (pi_array, in_circle_x, in_circle_y, out_circle_x, out_circle_y)

deviation = 1
presicion = 0.1
iteration = 1

while deviation >= (presicion / 1.96):
    pi_array, in_circle_x, in_circle_y, out_circle_x, out_circle_y = crear_muestra(tries)
    deviation = statistics.stdev(pi_array)
    variance = statistics.variance(pi_array)
    mean = statistics.mean(pi_array)

    print(f'------------------       Iteration number: {(iteration)}      ------------------')
    print(f'Standard deviation: {round(deviation, 5)}, Variance: {round(variance, 5)}, pi estimated: {round(mean, 5)}')
    print(f'Number of attempts: {tries}, Number of points: {puntos}\n\n')

    puntos *= 10
    tries *= 10
    iteration += 1

output_file("line.html")
plot = figure(width=600, height=600)  
plot.circle(in_circle_x, in_circle_y, size=5, color="red", alpha=0.5)
plot.circle(out_circle_x, out_circle_y, size=5, color="navy", alpha=0.5)
show(plot)
