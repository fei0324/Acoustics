import math
import numpy as np


from stl import mesh

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
	#print(points)
	#print(len(points))

	triangleSet = []
	x = 0
	y = 2**n

	for i in range(2**n+1, 1, -1):
		for j in range(x,y):

			tri = []
			tri.append(points[j])
			tri.append(points[j+1])
			tri.append(points[j+i])
			triangleSet.append(tri)

		x = x+i
		y = y+i-1

		for k in range(x,y):

			tri = []
			tri.append(points[k])
			tri.append(points[k+1])
			tri.append(points[k+1-i])
			triangleSet.append(tri)

	norVecSet = []

	for i in range(len(triangleSet)):
		norVecSet.append(unitNorVec)


	return points, triangleSet, norVecSet

"""
points, triangleSet, norVecSet = barycentric(np.array([1,1,1]),np.array([2,2,2]),np.array([3,4,2]),1)
print(len(triangleSet))
print(len(norVecSet))
print(triangleSet)
print(norVecSet)
"""


"""
sphere_mesh = mesh.Mesh.from_file('sphere_5.stl')

totalTriangleSet = []
totalNorVecSet = []
for i in range(len(sphere_mesh.vectors)):
	points, triangleSet, norVecSet = barycentric(sphere_mesh.vectors[i][0], sphere_mesh.vectors[i][1], sphere_mesh.vectors[i][2],1)
	print(len(triangleSet))
	print(len(norVecSet))

	for j in range(len(triangleSet)):
		totalTriangleSet.append(triangleSet[j])
		totalNorVecSet.append(norVecSet[j])

print(len(sphere_mesh.vectors))
print(len(totalTriangleSet))
print(len(totalNorVecSet))
"""