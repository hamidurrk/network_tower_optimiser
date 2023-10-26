import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.interpolate import griddata
import csv
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

x = []
y = []
signal_strength = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
        signal_strength.append(int(row[2]))
        
x = np.array(x)
y = np.array(y)
signal_strength = np.array(signal_strength)

# Clustering
data = np.column_stack((x, y))
kmeans = KMeans(n_clusters=12)  # Change the number of clusters as needed
kmeans.fit(data)
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Interpolation
grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]
grid_z = griddata((x, y), signal_strength, (grid_x, grid_y), method='cubic')

# Plotting
plt.figure(figsize=(10, 8))
plt.imshow(grid_z.T, extent=(min(x), max(x), min(y), max(y)), origin='lower')
plt.title('Interpolated Signal Strength')
plt.colorbar(label='Signal Strength')

# Add cluster centers and boundaries
for i in range(len(centers)):
    plt.scatter(centers[i][0], centers[i][1], s=300, c='red')  # plot cluster centers
    cluster_data = data[labels == i]
    radius = max(np.sum((cluster_data - centers[i])**2, axis=1))**0.5
    circle = plt.Circle((centers[i][0], centers[i][1]), radius, fill=False)
    plt.gca().add_patch(circle)

plt.show()


