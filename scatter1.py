
import sys
import numpy as np

if len(sys.argv) != 3:
    print('usage:', sys.argv[0],'data_file label_file')
    sys.exit()

X = np.genfromtxt(sys.argv[1], delimiter =',', autostrip = True)

#print("X=", X)

n,m = X.shape

Y = np.genfromtxt(sys.argv[2])
#print("Y=", Y)

s1 = np.zeros((1,m))
s2 = np.zeros((1,m))
s3 = np.zeros((1,m))

m1 = 0
m2 = 0
m3 = 0

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

S1 = np.zeros((m,m))
S2 = np.zeros((m,m))
S3 = np.zeros((m,m))

for i, x in enumerate(X):
    if Y[i] == 1:
        S1 += np.dot((x-mu1).T, x-mu1)
    if Y[i] == 2:
        S1 += np.dot((x-mu2).T, x-mu2)
    if Y[i] == 3:
        S1 += np.dot((x-mu3).T, x-mu3)

S = S1 + S2 + S3

#rint("S", S)

evals, evecs = np.linalg.eigh(S)

idx = np. argsort ( evals )[:: 1]
evals = evals [idx]
evecs = evecs [:, idx]
r = 2
V_r = evecs[: ,:r]
#print ("V_r=",V_r)

D = np.dot(X, V_r)

np.savetxt ('scatter1.txt', D, delimiter =',')

#min_W = np.dot(np.dot(V_r.T, S),V_r)

#print('The minimum of within-class scatter is :', min_W)
        
        
        
        
        
        
        
