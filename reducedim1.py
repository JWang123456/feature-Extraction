import sys
import numpy as np

if len(sys.argv) != 5 :
    print('usage : ', sys.argv[0], 'data_file labels_file reducedim1_vector_file reducedim1_reduced_data_file')
    sys.exit()


first = sys.argv[1]
# second = sys.argv[2]

DATA = np.genfromtxt(first, delimiter=',', autostrip=True) # strip spaces

# LABLE = np.genfromtxt(second, delimiter=',', autostrip=True) # strip spaces
# print("LABLE=", LABLE)


# computing SVD
# C = U S Vt
U,s,Vt = np.linalg.svd(DATA)
# print("U=", U, "\n s=", s, "\n Vt=",Vt)
# print("Vt=",Vt)

# matrix inverse and pseudo inverse
A_tr = np.transpose(Vt)
# print("A_inv=", A_inv, "\nA_pinv=",A_pinv)


# extract the 2 dominant eigenvectors
r = 2
V_r = A_tr[:r,:]
# print("V_r=",V_r) # get first r eigenvectors

DATA_tr = np.transpose(DATA)
# print('DATA', DATA, '\n' 'DATA-INV', DATA_tr)

def matrixmult (A, B):
    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C

x = matrixmult(V_r,DATA_tr)

res = np.transpose(x)

# save output in comma separated filename.txt. filename depends on the program
np.savetxt(sys.argv[4], res, delimiter=',')
np.savetxt(sys.argv[3], V_r, delimiter=',')