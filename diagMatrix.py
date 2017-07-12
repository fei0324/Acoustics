import numpy as np 
"""
	goal: to take the position vectors and the constant matrix and output the diagonal terms for the eigen value problem
	input: position vectors in a 3XN matrix
		   constant terms in a NXN matrix
	output: a 3NX3N matrix with zeros everywhere but the diagonal 3 by 3 blocks
"""

def Dmat(pterms,Mij):
	n = len(pterms)
	dim = len(pterms[0])
	#n is the number of masses
	#dim is the number of terms in the vectors
	nn = dim*n
	Dmat = np.zeros((nn,nn),dtype=complex)
	for i in range(0,nn):
		if i % dim == 0:
				#k is what block we are in
				k = i/dim 
				#cooi is the coordinate of the effected mass
				for cooi in range(0,dim):
					#cooj is the coordinate of the effecting mass
					for cooj in range(0,dim):
						b = 0
						#effmass is which mass is doing the effecting
						for effmass in range(0,n):
							#the algorythmn should run through all the different masses for each term with the coorisponding coordinates
							a = Mij[k,effmass]*((pterms[k][cooi]-pterms[effmass][cooi])*(pterms[k][cooj]-pterms[effmass][cooj]))
							b= b+a

						Dmat[i+cooi][i+cooj] = b
	return Dmat
"""
original test data
shows proper symetry in 3 by 3 blocks and zeros in the right places for 3 dementional vector inputs.
term [0][1]for Dmat of test 1 should be 650 and is
"""
Ptermstest1 = [np.array([0,0,0]),np.array([5,5,5]),np.array([10,0,-10]),np.array([-5,-30,2])]
Mijtest1 = np.matrix([[0,2,3,4],[5,0,7,8],[9,10,0,12],[13,14,15,0]])
print Dmat(Ptermstest1,Mijtest1)


#new test imput to check the right number of terms and the right kind of symetry given a more than 3 dementional input
#gives right sized matrix with right sized blocks and right placed zeros and correct symetry
Ptermstest2 = [np.array([0,0,0,0]),np.array([1,1,1,1]),np.array([-5,5,2,0]),np.array([6,7,8,-9])]
Mijtest2 = np.matrix([[0,2,3,4],[5,0,7,8],[9,10,0,12],[13,14,15,0]])
print Dmat(Ptermstest2,Mijtest2)