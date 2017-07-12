import numpy as np
#import  BarycentricSubdivision as bcy
#import MagnitudeMatrix as mx  
#import MagnitudeMatrixV2 as mx

""" goal of progarm:  create a function to make the non diagonal terms of the eigne value matrix for frequency
	inputs: pterms which is a (dimension x n) matrix of position vector inputs 
	and the Mij matrix is a (n x n) matrix of constants incorperating the spring constant and their magnitudes
	outputs: non diagonal terms of the eigenvalue matrix of (n*dim x n*dim) 
"""

"""
the algorithm may be optimizible by rewriting some of the for loops with modular arithmatic
has not been checked for correctness yet 
"""

"""
i = which row in imat
b = which colum in imat
g = effecting mass
k = effected mass
l = position in output matrix
j = position in output matrix

"""
def Imatrix(pterms, Mij):
	n = len(pterms)
	col = len(pterms[0])
	nn = n*col 	  
	Imat = np.zeros((nn,nn),dtype=complex) 

	for i in range(0,nn):
		if i % col == 0:	
			k = i/col	
			for l in range(i,i+col): 
				for b in range(0,nn): 
					if b % col == 0:
						g = b/col
						for j in range(b,b+col): 

							Imat[l,j] = (-1)*(Mij[k,g])*((pterms[k][(l-i)])-(pterms[g][(l-i)]))*((pterms[k][(j-b)])-(pterms[g][(j-b)]))

	return Imat

def otherTermMat(positions, Mij):

	OTMat = np.zeros((3*len(Mij),3*len(Mij)),dtype=complex)

	# i, j for Mij index, a, b for OTMat index
	for a in range(3*len(Mij)):
		for b in range(3*len(Mij)):
			i = a/3
			j = b/3
			OTMat[a,b] = (-1)*Mij[i,j]*(positions[i][a%3]-positions[j][a%3])*(positions[i][b%3]-positions[j][b%3])
	return OTMat

# test data
positions = [np.array([10,0,0]),np.array([0,5,-10]),np.array([-7.5,-10,0])]
Mij = np.matrix([[0,5,11],[-5,0,3],[-11,-3,0]])


print Imatrix(positions, Mij)
print("New one!!!")
print otherTermMat(positions, Mij)
   


