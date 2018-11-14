# Template program.
# Input: two files. data and labels.
# Data is a matrix of size nxm. labels is an array of size n.
# The labels are 1,2,3

import sys
import numpy as np

if len(sys.argv) != 5 :
    print('usage : ', sys.argv[0], 'data_file labels_file pca_iris_vec.csv pca_iris_reduced_data.csv')
    sys.exit()

# read the files for the matrices Xt and y. Xt is nxm, y is nx1
# use these to calculate two vectors v1, v2 each of size m
# Compute the projections of Xt on v1,v2 for the matrix D of size nx2

first = sys.argv[1]
second = sys.argv[2]

DATA = np.genfromtxt(first, delimiter=',', autostrip=True) # strip spaces

LABLE = np.genfromtxt(second, delimiter=',', autostrip=True) # strip spaces
# print("LABLE=", LABLE)


# computing SVD
# C = U S Vt
U,s,Vt = np.linalg.svd(DATA)
# print("U=", U, "\n s=", s, "\n Vt=",Vt)
print("Vt=",Vt)

# matrix inverse and pseudo inverse
A_inv = np.linalg.inv(Vt)
# print("A_inv=", A_inv, "\nA_pinv=",A_pinv)


# extract the 2 dominant eigenvectors
r = 2
V_r = A_inv[:r,:]; print("V_r=",V_r) # get first r eigenvectors

DATA_inv = np.linalg.pinv(DATA)
# print(DATA_inv)

def matrixmult (A, B):
    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C

x = matrixmult(V_r,DATA_inv)

res = np.linalg.pinv(x)

Vt = np.matrix('1 0 0 0 0 0; 0 1 0 0 0 0')
D = np.matrix('1 1; 2 2; 3 3; 4 4; 5 0')
D = np.matrix('1 1; 2 2; 3 3; 4 4; 5 0')

# save output in comma separated filename.txt. filename depends on the program
np.savetxt(sys.argv[4], res, delimiter=',')
np.savetxt(sys.argv[3], V_r, delimiter=',')


