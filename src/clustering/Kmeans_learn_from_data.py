#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ K-Means Clustering Algorithm ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=============================================================================================
# Importing necessary libaries

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.rcParams['figure.figsize'] = (16, 9)


X, y = make_blobs(n_samples=800, n_features=3, centers=4)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
# Creating a sample dataset with 4 clusters

# Creating a dummy dataset with 4 clusters

# Initializing KMeans
kmeans = KMeans(n_clusters=4)
# Initializing KMeans

kmeans = kmeans.fit(X)
# Fitting with inputs


labels = kmeans.predict(X)
# Predicting the clusters


C = kmeans.cluster_centers_
# Getting the cluster centers

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='#050505', s=1000)