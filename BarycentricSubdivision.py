import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
	#print(unitNorVec)
	print(points)
	#print(len(points))

	return (points, unitNorVec)

def plotP_V(points, unitNorVec):

	"""
	Plot all the subdivision points and the unit normal vectors

	Input: points and unitNorVec returned from the barycentric function

	Output: A 3d plot of points and vectors
	"""

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	xs = []
	ys = []
	zs = []

	u = unitNorVec[0]
	v = unitNorVec[1]
	w = unitNorVec[2]

	for i in range(0, len(points)):
		xs.append(points[i][0])
		ys.append(points[i][1])
		zs.append(points[i][2])

	ax.plot(xs, ys, zs, 'o')
	ax.quiver(xs, ys, zs, u, v, w, length=0.2, normalize=True)
	ax.legend()

	plt.show()

pt1 = np.array([0,0,1])
pt2 = np.array([0,1,0])
pt3 = np.array([1,0,0])

points, unitNorVec = barycentric(pt1, pt2, pt3, 1)
plotP_V(points, unitNorVec)