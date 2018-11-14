
import numpy as np
import sys

if len(sys.argv) != 5:
    print('usage:', sys.argv[0],'data_file label_file scatter1_iris_vec.csv scatter1_iris_reduced_data.csv')
    sys.exit()

X = np.genfromtxt(sys.argv[1], delimiter = ',', autostrip = True)
Y = np.genfromtxt(sys.argv[2])
n,m = X.shape

W1 = np.zeros((m,m))
W2 = np.zeros((m,m))
W3 = np.zeros((m,m))
V= np.zeros((m,m))

s1 = np.zeros((1,m))
s2 = np.zeros((1,m))
s3 = np.zeros((1,m))
s = np.zeros((1,m))

m1 = 0
m2 = 0
m3 = 0
m = 0


for i, x in enumerate (X):
    if Y[i] == 1:
        s1 += x
        m1 += 1
    if Y[i] == 2:
        s2 += x
        m2 += 1
    if Y[i] == 3:
        s3 += x
        m3 += 1

mu1 = s1/m1
mu2 = s2/m2
mu3 = s3/m3

for i, x in enumerate(X):
    s += x
    m += 1
mu = s/m

B = np.dot((mu - mu1).T,mu - mu1) * m1
B += np.dot((mu - mu2).T, mu - mu2) * m2
B += np.dot((mu - mu3).T, mu - mu3) * m3

for i, x in enumerate(X):
    if Y[i] == 1:
        W1 += np.dot((x-mu1).T, x-mu1)
    if Y[i] == 2:
        W1 += np.dot((x-mu2).T, x-mu2)
    if Y[i] == 3:
        W1 += np.dot((x-mu3).T, x-mu3)

W = W1 + W2 + W3
W_inv = np.linalg.inv(W)

C = np.dot(W_inv, B)

#print("C",C)

w, e = np.linalg.eigh(C)
idx = np.argsort(w)[:: -1]
e = e[:,idx]
w = w[idx]
r = 2
V_r = e[:,:r]

D = np.dot(X, V_r)

np.savetxt (sys.argv[3], V_r, delimiter =',')
np.savetxt (sys.argv[4], D, delimiter =',')

#vec = np.dot(np.dot(evecs,V_inv),V_r)
#print("max_ratio_vector is:", vec)

#max_ratio = np.dot(np.dot(vec.T, B),vec) / np.dot(np.dot(vec.T, W),vec)
#print("maximum ratio of between-class scatter and within-class scatter is:" , max_ratio)










