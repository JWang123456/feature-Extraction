# Template program.
# Input: two files. data and labels.
# Data is a matrix of size nxm. labels is an array of size n.
# The labels are 1,2,3

import sys
import numpy as np

if len(sys.argv) != 3 :
    print('usage : ', sys.argv[0], 'data_file labels_file ')
    sys.exit()

# read the files for the matrices Xt and y. Xt is nxm, y is nx1
# use these to calculate two vectors v1, v2 each of size m
# Compute the projections of Xt on v1,v2 for the matrix D of size nx2

first = sys.argv[1]
second = sys.argv[2]

DATA = np.genfromtxt(first, delimiter=',', autostrip=True) # strip spaces

LABLE = np.genfromtxt(second, delimiter=',', autostrip=True) # strip spaces
# print("LABLE=", LABLE)

def matrixsubtract (A, b):
    C = [[0 for row in range(len(A[0]))] for col in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
                C[i][j] = A[i][j] - b
    return C

def matrixavg (A):
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
                sum = sum + A[i][j]
    return sum/(len(A)*len(A[0]))

avg = matrixavg(DATA)
print(avg)
Y = matrixsubtract (DATA, avg)

# Example: computing the covariance matrix of X
# mu = np.mean(X, axis=1)
# Xc = X - mu;  print("Xc=",Xc)
# C = Xc*Xc.T;  print("C=",C)

Y_inv = np.linalg.pinv(Y)

def matrixmult (A, B):
    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C

M = matrixmult(Y_inv, Y)

def matrixdiv (M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = M[i][j]/len(Y)
    return M

C = matrixdiv(M)

evals,evecs = np.linalg.eigh(C) 
# print("evals=", evals, "\n" " evecs=", evecs)

idx = np.argsort(evals)[::-1] # sort in reverse order
evals = evals[idx]
evecs = evecs[:,idx]
# print("evals=", evals, "\n" "\n" " evecs=", evecs) # evectors are the cols of evecs


# extract the 2 dominant eigenvectors
r = 2
V_r = evecs[:r,:]; print("V_r=",V_r) # get first r eigenvectors

x = matrixmult(V_r,Y_inv)

res = np.linalg.pinv(x)
# print(C)
# # computing SVD
# # C = U S Vt
# U,s,Vt = np.linalg.svd(DATA)
# # print("U=", U, "\n s=", s, "\n Vt=",Vt)
# print("Vt=",Vt)

# # matrix inverse and pseudo inverse
# A_inv = np.linalg.inv(Vt)
# # print("A_inv=", A_inv, "\nA_pinv=",A_pinv)


# # extract the 2 dominant eigenvectors
# r = 2
# V_r = A_inv[:r,:]; print("V_r=",V_r) # get first r eigenvectors

# DATA_inv = np.linalg.pinv(DATA)
# # print(DATA_inv)

# def matrixmult (A, B):
#     C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 C[i][j] += A[i][k]*B[k][j]
#     return C

# x = matrixmult(V_r,DATA_inv)

# res = np.linalg.pinv(x)
# # A = np.matrix('1 2; 3 4; 5 6'); print("A=", A)
# # b = np.array([1,2]); print("b=", b)
# # # solve Ax=b
# # x = np.linalg.solve(A, b);  print("x=",x)
# # x = np.linalg.solve(V_r,DATA_inv); print("x=",x)


# Vt = np.matrix('1 0 0 0 0 0; 0 1 0 0 0 0')
# D = np.matrix('1 1; 2 2; 3 3; 4 4; 5 0')
# D = np.matrix('1 1; 2 2; 3 3; 4 4; 5 0')

# # save output in comma separated filename.txt. filename depends on the program
np.savetxt('reduced-b.txt', res, delimiter=',')
np.savetxt('V-b.txt', V_r, delimiter=',')



