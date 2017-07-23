import numpy as np
import unittest
import math 
import diagMatrix as Dmat


class DMatrixFunctionTestCase(unittest.TestCase):

	"""unit test for the D matrix code 
		should contain tests for symetry specific values and dementions
	"""
	
	def setUp(self):
		self.pterms1 = [np.array([0,0,0]),np.array([5,5,5]),np.array([10,0,-10]),np.array([-5,-30,2])]
		self.Mij1 = np.matrix([[0,2,3,4],[5,0,7,8],[9,10,0,12],[13,14,15,0]])

	#tests the length of the matrix and its dementions 
	def test_size(self):
		M = Dmat.Dmat(self.pterms1,self.Mij1)
		print("testing size of matrix")
		self.assertEqual(len(M), len(self.pterms1[0])*len(self.pterms1), msg="wrong size matrix.")

	#tests for proper symetry 
	def test_symetry(self):
		M = Dmat.Dmat(self.pterms1,self.Mij1)
		print("testing symetry")
		for i in range(0,len(M)):
			for j in range(0,len(M)):
				self.assertEqual(M[i][j], M[j][i], msg="symetry test failed.")
	#test for zeros
	"""def Test_zeros(self)
		M = Dmat.Dmat(self.pterms1,self.Mij1)
		print("testing for zero placements")
			for i in range (0,len(M))
			"""
	#test for specific cases
	def Specific_Value_test(self):
		M = Dmat.Dmat(self.pterms1,self.Mij1)
		print("testing specific values")
		self.assertEqual(M[0][1],650, msg="failed specific value test") 





if __name__ == '__main__':
	unittest.main()