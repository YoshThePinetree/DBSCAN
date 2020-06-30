import numpy as np
import matplotlib.pyplot as plot
import DissimilarityMatrix
import NeighborSearch

# Data loading
filename = "C:/PythonIO/Input/xor3.txt"
data = np.loadtxt(filename)

# Parameters Initiation
n, d = data.shape       # the no. of data, the no. of dimension
r = 0.5                 # radius of the data point for clustering
minPts = 10              # the minimum criterion for the core point
dist = "Euclid"         # the distance metric
D = DissimilarityMatrix.DissMat(data, n, d, dist)    # the dissimilarity matrix
D = D + D.T
U = np.zeros(n)         # cluster membership vector
V = np.zeros((n,n))     # reachable points matrix

NB = NeighborSearch

################
#### DBSCAN ####
################
print(D)
V = NB.Search(D, V, n, r)
L = NB.Core(V, U, n, minPts)
print(L)

# Plot data
markers1 = ["o", "x", "*", "^", "<", ">", "1", "2", "3"]
for i in range(len(L)):
    L_list = list(L[i])
    plot.scatter(data[L_list,0], data[L_list,1], marker=markers1[i])


