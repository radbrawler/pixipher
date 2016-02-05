import numpy as np

p = 1; q = 1
Arnold = np.matrix([[1,p],[q,p*q+1]])
X2 = np.zeros(shape=(2,1))
X1 = np.matrix([[1], [1]])
N = 3
print(Arnold)

for i in range(N):
    for j in range(N):
        # print(X1)
        X2 = np.dot(Arnold, [[i+1], [j+1]])%N
        X1 += [[1], [0]]
        print(X2[0][0]+1, X2[1][0]+1, i+1, j+1)
    X1 += [[0], [1]]


