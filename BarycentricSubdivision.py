import math
import numpy as np

def barycentric(pt1, pt2, pt3, n):

	"""
	Convert STL data into unit normal vectors and points on the triangles

	Input: Triangles (three 3d points) (3 numpy arrays)
		   a number of subdivisions to perform
	Output: Points on those triangles
			unit normal vectors points
	"""

	# find unit normal vector given three points on a plane
	vectorU = pt2 - pt1
	vectorV = pt3 - pt1
	normalVector = np.cross(vectorU, vectorV)
	#print(normalVector)
	unitNorVec = normalVector/np.linalg.norm(normalVector)
	#print(unitNorVec)

	# find subdivision points in barycentric coordinates
	points = [] #points includes the vertices of the original triangle
	for i in range(0, 2**n+1):
		for j in range(0, 2**n+1-i):
			points.append(pt1 + (i/2.**n)*vectorU + (j/2.**n)*vectorV)
			#print(points)
	#print(len(points))
	
	return unitNorVec, points

pt1 = np.array([1,0,0])
pt2 = np.array([0,1,0])
pt3 = np.array([0,0,1])
barycentric(pt1, pt2, pt3, 2)
