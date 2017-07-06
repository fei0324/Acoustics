import numpy as np
#import  BarycentricSubdivision as bcy
#import MagnitudeMatrix as mx  
#import MagnitudeMatrixV2 as mx

""" goal of progarm:  create a function to make the non diagonal terms of the eigne value matrix for frequency
	inputs: pterms which is a (dimenstion x n )matrix of position vector inputs 
	and the Mij matrix is a (n x n) matrix of constants incorperating the spring cconstant and their magnatudes
	outputs: non diagonal terms of the eignevalue matrix of (n*dim x n*dim) 
"""

"""
the algorithum may be optimizible by rewriting some of the for loops with modular arithmatic
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
	n, col = pterms.shape
	nn = n*col 	  
	Imat = np.zeros((nn,nn)) 

	for i in range(0,nn):
		if i % col == 0:	
			k = i/col	
			for l in range(i,i+col): 
				for b in range(0,nn): 
					if b % col == 0:
						g = b/col
						for j in range(b,b+col): 

							Imat[l,j] = (-1)*(Mij[k,g])*((pterms[k,(l-i)])-(pterms[g,(l-i)]))*((pterms[k,(j-b)])-(pterms[g,(j-b)]))

	return Imat

# test data
pterms = np.matrix([[10,0,0],[0,5,-10],[-7.5,-10,0]])
Mij = np.matrix([[0,5,11],[-5,0,3],[-11,-3,0]])


print Imatrix(pterms, Mij)
   


