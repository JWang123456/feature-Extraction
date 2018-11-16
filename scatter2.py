
import numpy as np
import sys

if len(sys.argv) != 5:
    print('usage:', sys.argv[0],'data_file label_file scatter_vec.csv scatter_reduced_data.csv')
    sys.exit()
    
X = np.genfromtxt(sys.argv[1], delimiter = ',', autostrip = True)
Y = np.genfromtxt(sys.argv[2])

n,m = X.shape

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

#print("B", B)

evals, evecs = np.linalg.eigh(B)
idx = np. argsort ( evals )[:: -1] # sort in reverse order
evals = evals [idx]
evecs = evecs [:, idx]
r = 2
V_r = evecs[: ,:r]
#print ("V_r=",V_r)

D = np.dot(X, V_r)

np.savetxt (sys.argv[3], V_r, delimiter =',')
np.savetxt (sys.argv[4], D, delimiter =',')

#max_B = np.dot(np.dot(V_r.T, B),V_r)

#print("The maximum of between-class scatter is :", max_B)



