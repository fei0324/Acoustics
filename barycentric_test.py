import unittest
import numpy as np
import math

import BarycentricSubdivision

class BarycentricTestCase(unittest.TestCase):
	def setUp(self):
		self.pt1 = np.array([0,0,1])
		self.pt2 = np.array([0,1,0])
		self.pt3 = np.array([1,0,0])
		self.n = 4

	def test_type(self):
		points, unitNorVec = BarycentricSubdivision.barycentric(self.pt1, self.pt2, self.pt3, 1)
		print("Testing type of 'points'.")
		self.assertTrue(type(points) == list, msg="Type of 'points' is incorrect.")
		print("Testing type of unit normal vector.")
		self.assertTrue(type(unitNorVec) == np.ndarray, msg="Type of unit normal vector is incorrect.")


	def test_sizeOfPoints(self):

		for i in range(self.n):

			points, unitNorVec = BarycentricSubdivision.barycentric(self.pt1, self.pt2, self.pt3, i)
			numbOfPts = sum(range(2**i+2))

			print("Testing the size of the point list with " + str(i) + " subdivisions.")
			#verify the length of subdivision point list
			self.assertEqual(len(points), numbOfPts, msg="Incorrect number of subdivision points")

	def test_unitNorVec(self):

		points, unitNorVec = BarycentricSubdivision.barycentric(self.pt1, self.pt2, self.pt3, 1)
		#verify normal vector
		print("Testing unit normal vectors.")
		self.assertTrue(abs(unitNorVec[0]-(-1/math.sqrt(3)))<1e-5, msg="Unit normal vector first component incorrect.")

		#verify second component of points is correct
		#self.assertTrue(abs(points[1][0]-0.5)<1e-5, msg="Incorrect subdivision.")

if __name__ == '__main__':
	unittest.main()