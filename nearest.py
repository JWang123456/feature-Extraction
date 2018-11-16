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
reduced_data_file = sys.argv[1]
vector_file = sys.argv[2]
labels_file = sys.argv[3]
queried_point_file = sys.argv[4]
label = int(sys.argv[5])
output_file = sys.argv[6]

if label == -1:
    reduced_data_file = 'reducedim1_' + reduced_data_file
    vector_file = 'reducedim1_' + vector_file
    #print("ii")
    #output_file = 'case1_' + output_file
else:
    reduced_data_file = 'reducedim2_' + reduced_data_file
    vector_file = 'reducedim2_' + vector_file
    #print("oo")
    #output_file = 'case2_' + output_file

with open(reduced_data_file,"r") as filestream:
	reduced_data = np.loadtxt(filestream, delimiter=',')
#n,m = reduced_data.shape

with open(vector_file,"r") as filestream:
	reduced_vector = np.loadtxt(filestream, delimiter=',')

# print(reduced_vector)
with open(labels_file,"r") as filestream:
	labels = np.loadtxt(filestream, delimiter=',')
unique_labels, counts_labels = np.unique(labels, return_counts=True)
#print(unique_labels)

with open(queried_point_file,"r") as filestream:
	queried_point = np.loadtxt(filestream, delimiter=',')

print("queried_point", queried_point)
print("reduced_vector", reduced_vector.T)
reduced_queried_point = np.dot(queried_point, reduced_vector.T)

# print(reduced_queried_point)
#print(reduced_data[0])
distance = sys.maxsize
#print(distance)

index = []
# print(index)

for i, data in enumerate(reduced_data):
	if label == -1:
		d = np.square(data[0] - reduced_queried_point[0]) + np.square(data[1] - reduced_queried_point[1])
		if d == distance:
			index.append(i)
		if d < distance:
			index = []
			index.append(i)
			distance = d
			#print(index)
			#print(distance)
			#print(type(label))
			#print(type(labels[i]))
			#print(label == labels[i])
	else:
		if label == labels[i]:
			d = np.square(data[0] - reduced_queried_point[0]) + np.square(data[1] - reduced_queried_point[1])
			#print(data)
			#print(reduced_queried_point)
			#print(d)
			if d == distance:
				index.append(i)
			if d < distance:
				index = []
				index.append(i)
				distance = d
				#print(index)
				#print(distance)

# print(index)

np.savetxt(output_file, index, fmt='%d', delimiter=',')

#print(index)
#print(distance)


































#queried_point_file = sys.argv[1]
#with open(queried_point_file,"r") as filestream:
	#queried_point = np.loadtxt(filestream, delimiter=',')

# return index of nearest neighbor 
#nn_idx = np.array([10])

#print(nn_idx)

# Output file name should be read from command line.
#output_file = 'nn_idx.csv' 

# save output in comma separated filename.txt.
#np.savetxt(output_file, nn_idx, delimiter=',')



#np.savetxt(sys.argv[6], nn_idx, delimiter=',')
