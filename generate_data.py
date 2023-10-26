import csv
import random
import math

x_start, x_end = 23.749249, 23.724104   # longitude
y_start, y_end = 90.369372, 90.404603   # latitude
signal_start, signal_end = 0, 30
size = 50
dim = round(math.sqrt(size))

x_step = (x_end - x_start) / (dim)
y_step = (y_end - y_start) / (dim)

data = []

for i in range(dim):
    x = round(x_start + i * x_step, 6)
    for j in range(dim):
        y = round(y_start + j * y_step, 6)
        signal_strength = random.randint(signal_start, signal_end)
        data.append([x, y, signal_strength])

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Longitude", "Latitude", "Signal_Strength"])
    writer.writerows(data)
