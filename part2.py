# Template program for nearest.py.
# Input: five input arguments. reduced_file Vector_file labels_file queried_point_file label
# one output arguments, output_file
# reduced_file is a matrix of size nx2. Vector_file is a matrix of 2xm. 
# labels_file is an array of size n.The labels are 1,2,3

# queried_point is an 1xm. label is an integer.
# If lable is -1, it means finding the result for reducedim1.py.
# Otherwise, it means finding the result for reducedim2.py.

import sys
import numpy as np

if len(sys.argv) != 7 :
    print('usage : ', sys.argv[0], 'reduced_data_file vector_file labels_file queried_point_file label output_file')
    sys.exit()

# read the files for the matrices reduced_Xt, vector, labels, queried_point and label..

# return index of nearest neighbor 
nn_idx = np.array([10])

# Output file name should be read from command line.
output_file = 'nn_idx.csv' 

# save output in comma separated filename.txt.
np.savetxt(output_file, nn_idx, delimiter=',')
