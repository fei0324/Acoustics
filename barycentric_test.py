import unittest
import numpy as np
import math

import BarycentricSubdivision

class BarycentricTestCase(unittest.TestCase):

	def test_barycentric(self):
		"""test for correct subdivisions and normal vector"""
		pt1 = np.array([0,0,1])
		pt2 = np.array([0,1,0])
		pt3 = np.array([1,0,0])

		#verify normal vector
		points, unitNorVec = BarycentricSubdivision.barycentric(pt1, pt2, pt3, 1)
		self.assertTrue(abs(unitNorVec[0]-(-1/math.sqrt(3)))<1e-5, msg="Unit normal vector first component incorrect.")

		#verify second component of points is correct
		self.assertTrue(abs(points[1][0]-0.5)<1e-5, msg="Incorrect subdivision.")

if __name__ == '__main__':
	unittest.main()