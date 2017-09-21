import math
import numpy as np
from stl import mesh

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

import LSolver
import crossArea
import otherTermMat
import diagMatrix
import Mij

sphere_mesh = mesh.Mesh.from_file('sphere.stl')
triangleSet = sphere_mesh.vectors
triNormVecs = sphere_mesh.normals
forceVecs = np.zeros((len(triangleSet),3))


for i in range(len(forceVecs)):
	forceVecs[i] = -1*triNormVecs[i]*3

Llist, Lmat = LSolver.lengthSolver(triangleSet,triNormVecs,forceVecs)

positions = Mij.pointsFromSTL(triangleSet)


Mij = Mij.MijMat(10,Llist,triangleSet,positions)
OTMat = otherTermMat.otherTermMat(positions,Mij)
Dmat = diagMatrix.Dmat(positions,Mij)

BigMatrix = OTMat + Dmat
# w is the set of all eigenvalues
# v is the set of all eigenvectors, v[:,i] corresponds to w[i]
#w,v = np.linalg.eig(BigMatrix)
#print(w[1])
#print(v[:,1])
#print(len(v[:,1]))

# Plot eigenvectors
def plotEigenVectorCoor(BigMatrix, indexW, modClass):

	"""
	Plot each coordinate of each eigenvector on each points
	Plot the magnitude of eigenvector on points

	Input: BigMatrix = OTMat + Dmat
		   indexW = the index of eigenvalue and the corresponding index of the eigenvector
		   modClass = a number 0, 1 or 2 that dictates the coordinate (x, y or z) in the plot
	
	Output: Color coded object based ont he magnitude of the (coordinates of the) eigenvectors
	"""

	w, v = np.linalg.eig(BigMatrix)
	listOfCoor = np.zeros(50)
	indexOfList = 0

	for i in range(len(v[:,indexW])):
		if i%3 == modClass:

			listOfCoor[indexOfList] = v[i, indexW]
			indexOfList += 1

	#print v[:, indexW]
	return listOfCoor
	#print len(listOfCoor)

#plotEigenVectorCoor(BigMatrix, 1, 0)

def plotEigenVectorLength(BigMatrix, indexW):

	w, v = np.linalg.eig(BigMatrix)
	listOfLength = np.zeros(len(positions))
	indexOfList = 0

	for i in range(len(v[:,indexW])):
		if i%3 == 0:
			xyz = np.array([v[i,indexW], v[i+1,indexW], v[i+2,indexW]])

			listOfLength[indexOfList] = np.linalg.norm(xyz)
			indexOfList += 1

	return listOfLength
	#print len(listOfCoor)

listOfLength0 = plotEigenVectorLength(BigMatrix, 0)
listOfLength1 = plotEigenVectorLength(BigMatrix, 1)
listOfLength2 = plotEigenVectorLength(BigMatrix, 2)
listOfLength3 = plotEigenVectorLength(BigMatrix, 3)


fig = plt.figure()
ax0 = fig.add_subplot(221, projection='3d')
ax0.set_title("Eigenvector 0")
ax1 = fig.add_subplot(222, projection='3d')
ax1.set_title("Eigenvector 1")
ax2 = fig.add_subplot(223, projection='3d')
ax2.set_title("Eigenvector 2")
ax3 = fig.add_subplot(224, projection='3d')
ax3.set_title("Eigenvector 3")

xs = []
ys = []
zs = []

for i in range(len(positions)):
	xs.append(positions[i][0])
	ys.append(positions[i][1])
	zs.append(positions[i][2])

ax0.scatter(xs, ys, zs, c=listOfLength0, cmap=cm.cool)
ax1.scatter(xs, ys, zs, c=listOfLength1, cmap=cm.cool)
ax2.scatter(xs, ys, zs, c=listOfLength2, cmap=cm.cool)
ax3.scatter(xs, ys, zs, c=listOfLength3, cmap=cm.cool)

plt.show()

"""
print(BigMatrix)
print(len(BigMatrix))
print(BigMatrix[0])
print(BigMatrix[1])
#print(Dmat)
#print(len(Dmat))

plot a matrix
plt.imat()
plt.imshow() #real and imaginary separately or magnitude
"""
