import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.interpolate import griddata
import csv

x = []
y = []
signal_strength = []

with open('final_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
        signal_strength.append(float(row[2]))
        
x = np.array(x)
y = np.array(y)
signal_strength = np.array(signal_strength)

# print(x)
# print(y)
# print(signal_strength)

grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]

grid_z = griddata((x, y), signal_strength, (grid_x, grid_y), method='cubic')

# plt.figure(figsize=(10, 8))
# plt.imshow(grid_z.T, extent=(min(x), max(x), min(y), max(y)), origin='lower')
# plt.title('Interpolated Signal Strength')
# plt.colorbar(label='Signal Strength')

plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')
ax.plot_surface(grid_x, grid_y, grid_z, cmap='plasma')
plt.show()
# plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
