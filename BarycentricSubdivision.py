import math
import numpy as np

def barycentric(pt1, pt2, pt3, n):

	"""
	Convert STL data into unit normal vectors and points on the triangles

	Input: Triangles (three 3d points) (3 numpy arrays)?
		   a number of subdivisions to perform???
	Output: Points on those triangles
			unit normal vectors points
	"""

	# find unit normal vector given three points on a plane
	vector1 = pt1 - pt2
	vector2 = pt1 - pt3
	normalVector = np.cross(vector1, vector2)
	#print(normalVector)
	unitNorVec = normalVector/np.linalg.norm(normalVector)
	#print(unitNorVec)
	return unitNorVec

pt1 = np.array([1,1,1])
pt2 = np.array([-1,1,0])
pt3 = np.array([2,0,3])
barycentric(pt1, pt2, pt3, 0)
