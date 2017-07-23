import unittest
import numpy as np
import math
#import subdivision
import otherTermMat as Omat

class ImatTestCase(unittest.TestCase):

	def setUp(self):
		self.positions = [np.array([10,0,0]),np.array([0,5,-10]),np.array([-7.5,-10,0])]
		self.Mij = np.matrix([[0,5,11],[5,0,3],[11,3,0]])

	#tests that the 3x3 blocks of zeros are in correct place
	def test_zero(self):
		M = Omat.otherTermMat(self.positions, self.Mij)
		print("Testing diagonal zeros.")
		for i in range(0,len(M)):
			if i % 3 == 0:
					#k is what block we are in
					k = i/3 
					#cooi is the coordinate of the effected mass
					for cooi in range(0,3):
						#cooj is the coordinate of the effecting mass
						for cooj in range(0,3):
							self.assertEqual(M[i+cooi][i+cooj], 0, msg="Failed diagnoal zero test" )

	#tests the length of the matrix and its dementions 
	def test_size(self):
		M = Omat.otherTermMat(self.positions, self.Mij)
		print("testing size of matrix")
		self.assertEqual(len(M), 3*len(self.Mij), msg="wrong size matrix.")

	#tests for proper symetry 
	def test_symetry(self):
		M = Omat.otherTermMat(self.positions, self.Mij)
		print("testing symetry")
		for i in range(0,len(M)):
			for j in range(0,len(M)):
				self.assertEqual(M[i][j], M[j][i], msg="symetry test failed.")

	#test for specific cases
	def test_specificValue(self):
		M = Omat.otherTermMat(self.positions, self.Mij)
		print("testing specific values")
		self.assertEqual(M[0][3], -500, msg="failed specific value test") 
		self.assertEqual(M[0][4], 250, msg="failed specific values test")
		self.assertEqual(M[0][5], -500, msg="failed specific value test")
		self.assertEqual(M[0][6], -3368.75, msg="failed specific value test")
		self.assertEqual(M[0][7], -1925, msg="failed specific value test")
		self.assertEqual(M[0][8], 0, msg="failed specific value test")

if __name__ == '__main__':
	unittest.main()




