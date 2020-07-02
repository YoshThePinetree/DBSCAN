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
V = np.zeros((n,n))     # reachable points matrix

NB = NeighborSearch

################
#### DBSCAN ####
################
print(D)
V = NB.Search(D, V, n, r)
print(V)
L, C = NB.Core(V, n, minPts)
print(L)

# Plot data
markers1 = ["x", "*", "D", "^", "<", ">", "1", "2", "3"]
check = np.ones(n)
for i in range(len(L)):
    L_list = list(L[i])
    plot.scatter(data[L_list,0], data[L_list,1], marker=markers1[i])
    check[L_list] = 0

ind = np.where(check==1)
plot.scatter(data[ind,0], data[ind,1], marker="o", c="k")
