import numpy as np
import math


def Search(D, V, n, r):
    for i in range(n):
        count = 0
        for j in range(n):
            if (D[i,j] <= r) & (i != j):
                count += 1
                V[i,j] = 1
    return V


def Core(V, U, n, minPts):
    corelist = []   # list for core points
    clstset = []    # setlist for clusters
    check = np.zeros(n)
    subtract = np.zeros(n)
    sum = np.sum(V, axis=0)
    for i in range(n):
        if sum[i] >= minPts:
            corelist.append(i)
        else:
            check[i] = 1

    count = 0
    for i in range(n):
        if check[i] == 0:
            tmp = list(np.where(V[i,:]==1))
            tmp1 = []
            tmp1 = tup2list(tmp)
            tmp2 = set(tmp1)
            clstset.append(tmp2)

            for j in range(len(tmp[0])):
                check[tmp[0][j]] = 1
            check[i] = 1
            count += 1

    listnum = len(clstset)
    # while(1):
    check = np.zeros(listnum)
    dellist = lambda items, indices: [item for idx, item in enumerate(items) if idx not in indices]

    listnum1 = listnum
    while(1):
        i = 0
        while (i < listnum):
            clstlist = list(clstset[i])
            for j in range(len(clstset[i])):
                for k in range(listnum):
                    if i != k:
                        if clstlist[j] in list(clstset[k]):
                            clstset[i] = clstset[i] | clstset[k]
                            check[k] = 1

            ind = np.where(check==1)    # 統合されたクラスタ
            indlist = tup2list(ind)
            clstset = dellist(clstset, indlist)

            listnum = len(clstset)
            check = np.zeros(listnum)
            i += 1

        if listnum1 == listnum:
            break
        listnum1 = listnum

    return clstset

def tup2list(t):
    tmp = []
    for i in range(len(t[0])):
        tmp.append(t[0][i])

    return tmp