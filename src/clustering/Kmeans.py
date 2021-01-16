#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ K-Means Clustering Algorithm ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=============================================================================================
# Importing necessary libaries
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing the dataset on which you want to perform clustering
data = pd.read_csv('kmeans1.csv')
print("Input Data and Shape")
print(data.shape)
data.head()


f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='black', s=7)
# Getting the values and plotting it




def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

#Calculating the Euclidean Distance    

k = 3
# Number of clusters

C_x = np.random.randint(0, np.max(X)-20, size=k)
# X coordinates of random centroids

C_y = np.random.randint(0, np.max(X)-20, size=k)
# Y coordinates of random centroids

C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids")
print(C)


plt.scatter(f1, f2, c='#050505', s=7)
# Plotting along with the Centroids
plt.scatter(C_x, C_y, marker='*', s=200, c='g')


C_old = np.zeros(C.shape)
# To store the value of centroids when it updates

clusters = np.zeros(len(X))
# Cluster Lables(0, 1, 2)

error = dist(C, C_old, None)
# Error func. - Distance between new centroids and old centroids


while error != 0:
    # Loop will run till the error becomes zero
    # Assigning each value to its closest cluster
    for i in range(len(X)):
        distances = dist(X[i], C)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    # Storing the old centroid values
    C_old = deepcopy(C)
    # Finding the new centroids by taking the average value
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old, None)

colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')





from sklearn.cluster import KMeans


kmeans = KMeans(n_clusters=3)
# Number of clusters (2,3,5,10,X)

kmeans = kmeans.fit(X)

# Fitting the input data


labels = kmeans.predict(X)
# Getting the cluster labels

centroids = kmeans.cluster_centers_
# Centroid values

# Comparing with scikit-learn centroids
print("Centroid values")
print("Scratch")
print(C) 
#  This will print C From Scratch
print("sklearn")
print(centroids) 
# This will print From sci-kit learn