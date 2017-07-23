import numpy as np
import unittest
import math 
import isotropicMatrix as isoMat

"""unit test for the D matrix code 
		should contain tests for symetry specific values and dementions
"""
class isoMatrixFunctionTestCase(unittest.TestCase):	

	def setUp(self): 
		self.source1 = np.array([[0,0],[0,1]])
		self.sample1 = np.array([[-1,1],[1,1],[1,-1],[-1,-1]])
		self.source2 = np.array([[10,20,30], [1,2,4], [6,3,6]])
		self.sample2 = np.array([[0,0,0],[0,1,0],[2,1,0]])
		self.source3 = np.array([[0,0,0]])
		self.sample3 = np.array([[0,1,0],[1,0,0],[1,1,0]])

#tests for column values 
	def test_colums(self):
		M = isoMat.isotropicMatrix(1,self.source1,self.sample1)
		print("testing colums")
		for i in range(0,len(M)):
			if i < len(M)-1:
				self.assertEqual(M[i][0], M[i+1][0], msg="colum test failed.")

	# test for row values
	def test_row(self):
		M = isoMat.isotropicMatrix(1,self.source2,self.sample2)  
		print("testing rows values")
		self.assertEqual(M[1][1], M[2][1], msg="row test failed")	

	# test for specific values
	def test_specific(self):
		M = isoMat.isotropicMatrix(1,self.source3,self.sample3)  
		g = (-1/(4*math.pi))
		h = (math.cos(2*math.pi*math.sqrt(2)))/(4*math.pi*math.sqrt(2))
		l = (math.sin(2*math.pi*math.sqrt(2)))/(4*math.pi*math.sqrt(2))*(-1) 
		print("testing specific values")
		self.assertTrue(abs(M[2][0]-complex(h,l))<(1e-5+1e-5j), msg="specific test failed")

if __name__ == '__main__':
	unittest.main()

