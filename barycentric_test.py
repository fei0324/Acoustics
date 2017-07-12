import unittest
import numpy as np
import math

import subdivision

class BarycentricTestCase(unittest.TestCase):
	def setUp(self):

		self.pt1 = np.array([0,0,1])
		self.pt2 = np.array([0,1,0])
		self.pt3 = np.array([1,0,0])
		self.n = 3
		self.points, self.triangleSet, self.unitNorVec = subdivision.barycentric(self.pt1,self.pt2,self.pt3,self.n)

	def test_type(self):

		print("Testing type of 'points'.")
		self.assertTrue(type(self.points) == list, msg="Type of 'points' is incorrect.")
		print("Testing type of unit normal vector.")
		self.assertTrue(type(self.unitNorVec) == np.ndarray, msg="Type of unit normal vector is incorrect.")


	def test_sizeOfPoints(self):

		for i in range(self.n):

			points, triangleSet, unitNorVec = subdivision.barycentric(self.pt1, self.pt2, self.pt3, i)
			numbOfPts = sum(range(2**i+2))

			print("Testing the size of the point list with " + str(i) + " subdivisions.")
			#verify the length of subdivision point list
			self.assertEqual(len(points), numbOfPts, msg="Incorrect number of subdivision points")

	def test_pointInPoints(self):

		print("Testing individual points in the points list.")
		#verify x of the 5th point (index 4)
		self.assertTrue(abs(self.points[4][0]-0.5)<1e-5, msg="Incorrect subdivision.")
		#verify z of the 20th point (index 19)
		self.assertTrue(abs(self.points[19][2]-0.5)<1e-5, msg="Incorrect subdivision.")
		#verify y of the 31st point (index 30)
		self.assertTrue(abs(self.points[30][1]-0.5)<1e-5, msg="Incorrect subdivision.")

	def test_unitNorVec(self):

		#verify normal vector
		print("Testing unit normal vectors.")
		self.assertTrue(abs(self.unitNorVec[0]-(-1/math.sqrt(3)))<1e-5, msg="Unit normal vector first component incorrect.")

	def test_sizeOfTriangleSet(self):
		
		print("Testing size of triangle set.")
		numOfTriangles = 0
		for i in range(1, 2**(self.n+1), 2):
			numOfTriangles += i
		self.assertEqual(len(self.triangleSet), numOfTriangles, msg="Incorrect size for triangle set.")

	def test_pointInTriangleSet(self):

		print("Testing individual points in the triangle set.")
		#verify x of the second point in the 12th triangle (index 11)
		self.assertTrue(abs(self.triangleSet[11][1][0]-0.5)<1e-5, msg="Incorrect triangle triples.")
		#verify x of the third point in the 49th triangle (index 48)
		self.assertTrue(abs(self.triangleSet[48][2][0]-0.)<1e-5, msg="Incorrect triangle triples.")

	def test_triangleArea(self):
		
		triangleAreaSet = subdivision.triangleArea(self.triangleSet)
		print("Testing triangle area.")
		v1 = self.pt2 - self.pt1
		v2 = self.pt3 - self.pt1
		areaOftriangle = np.linalg.norm(np.cross(v1,v2))/2
		self.assertTrue(abs(areaOftriangle/len(self.triangleSet)-triangleAreaSet[0])<1e-5, msg="Incorrect triangle area.")


if __name__ == '__main__':
	unittest.main()