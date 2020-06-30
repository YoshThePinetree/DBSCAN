import numpy as np
import math


def DissMat(X, n, d, dist):
    Y = np.zeros((n, n))
    if dist == "Euclid":
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(d):
                    Y[i, j] += (X[i, k] - X[j, k]) ** 2
                Y[i, j] = math.sqrt(Y[i, j])

    return Y
