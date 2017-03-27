from __future__ import division
import numpy as np

fp = open('pca-data.txt','r')
k = 2

data = []
for line in fp.readlines() :
    line = line.split()
    data.append([float(line[0]),float(line[1]),float(line[2])])

data = np.mat(data)

Miu = np.mean(data, axis=0)

new_data = data - Miu

n,_ = np.shape(data)

Sigma = (new_data.T * new_data)/n

eigVal, eigVec = np.linalg.eig(Sigma)

idx =  eigVal.argsort()[::-1]

eigVal = eigVal[idx]
eigVec = eigVec[:,idx] 

U_terncate = eigVec[:,:k]
print "EigentVector:\n"+str(U_terncate)


Z = np.dot(data,U_terncate)

print "Data:\n"+str(Z)