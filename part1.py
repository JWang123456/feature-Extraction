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
print("DATA=", DATA)

LABLE = np.genfromtxt(second, delimiter=',', autostrip=True) # strip spaces
print("LABLE=", LABLE)


Vt = np.matrix('1 0 0 0 0 0; 0 1 0 0 0 0')
D = np.matrix('1 1; 2 2; 3 3; 4 4; 5 0')
D = np.matrix('1 1; 2 2; 3 3; 4 4; 5 0')

# save output in comma separated filename.txt. filename depends on the program
np.savetxt('reduced-a.txt', D, delimiter=',')
np.savetxt('V-a.txt', Vt, delimiter=',')


