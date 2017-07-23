import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh

import subdivision
import isotropicMatrix

def plotP_V(points, unitNorVec, ax):

	"""
	Plot all the subdivision points and the unit normal vectors

	Input: points and unitNorVec returned from the barycentric function

	Output: A 3d plot of points and vectors
	"""

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
	#ax.quiver(xs, ys, zs, u, v, w, length=0.2, normalize=True)

fig = plt.figure(figsize=plt.figaspect(0.5))
fig.suptitle("Test for Subdivision", fontsize = 18)
ax1 = fig.add_subplot(1,2,1,projection='3d')
ax1.set_title("Sphere STL Subdivision")
ax2 = fig.add_subplot(1,2,2,projection='3d')
ax2.set_title("Cylinder STL Subdivision")

sphere_mesh = mesh.Mesh.from_file('sphere.stl')
cylinder_mesh = mesh.Mesh.from_file('cylinder.stl')
plt.hold(True)

for i in range(len(sphere_mesh.vectors)):
	points, triangleSet, unitNorVec = subdivision.barycentric(sphere_mesh.vectors[i][0], sphere_mesh.vectors[i][1], sphere_mesh.vectors[i][2],3)
	triangleAreaSet = subdivision.triangleArea(triangleSet)
	plotP_V(points, unitNorVec, ax1)

for j in range(len(cylinder_mesh.vectors)):
	points1, triangleSet1, unitNorVec1 = subdivision.barycentric(cylinder_mesh.vectors[j][0], cylinder_mesh.vectors[j][1], cylinder_mesh.vectors[j][2],4)
	triangleAreaSet1 = subdivision.triangleArea(triangleSet1)
	plotP_V(points1, unitNorVec1, ax2)

plt.show()
print("Sphere points = " + str(len(points)))
print("Sphere triangles = " + str(len(triangleSet)))
print("Sphere triangle areas = " + str(len(triangleAreaSet)))
print("Cylinder points = " + str(len(points1)))
print("Cylinder triangles = " + str(len(triangleSet1)))
print("Cylinder triangle areas = " + str(len(triangleAreaSet1)))

def plotIsoMat(isoMat):

	matToArray = np.squeeze(np.asarray(isoMat))
	imaginaryArray = matToArray*-1j

	fig1 = plt.figure(2)
	fig1.suptitle("Isotropic Matrix Graph", fontsize = 18)
	plt.subplot(211)
	plt.plot(points, matToArray, 'bo')
	plt.subplot(212)
	plt.plot(points, imaginaryArray, 'r--')

	plt.show()

points = np.linspace(1,50,50)
isoMat = isotropicMatrix.isotropicMatrix(10, points, np.array([0]))
plotIsoMat(isoMat)