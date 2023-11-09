import csv
import random
import math

x_start, x_end = 23.7492490, 23.7241040   # longitude
y_start, y_end = 90.3693720, 90.4046030   # latitude
signal_start, signal_end = 0, 30
size = 5000
dim = round(math.sqrt(size))

x_step = (x_end - x_start) / (dim)
y_step = (y_end - y_start) / (dim)

data = []

for i in range(dim):
    x = round(x_start + i * x_step, 7)
    for j in range(dim):
        y = round(y_start + j * y_step, 7)
        signal_strength = random.randint(signal_start, signal_end)
        data.append([x, y, signal_strength])

with open('data2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Longitude", "Latitude", "Signal_Strength"])
    writer.writerows(data)

# from scipy stats.norm
