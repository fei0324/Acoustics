import math
import numpy as np
from stl import mesh

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

import subdivision
import LSolver
import crossArea
import otherTermMat
import diagMatrix
import Mij

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

def plotEigenVectorLength(BigMatrix, indexW, positions):

	w, v = np.linalg.eig(BigMatrix)
	listOfLength = np.zeros(len(positions))
	indexOfList = 0

	for i in range(len(v[:,indexW])):
		if i%3 == 0:
			xyz = np.array([v[i,indexW], v[i+1,indexW], v[i+2,indexW]])

			listOfLength[indexOfList] = np.linalg.norm(xyz)
			indexOfList += 1

	return listOfLength

def plot(filename,n):

	"""
	Input: filename needs to be in '.stl' format ex. filename = 'sphere.stl'
		   n = the number of the times of division
	"""

	file_mesh = mesh.Mesh.from_file(filename)

	oriTriangleSet = file_mesh.vectors
	#triNormVecs = file_mesh.normals

	triangleSet = []
	triNormVecs = []

	for i in range(len(oriTriangleSet)):
		points, singleTriangleSet, singleNorVecSet = subdivision.barycentric(oriTriangleSet[i][0], oriTriangleSet[i][1], oriTriangleSet[i][2],n)
		#print(len(triangleSet))
		#print(len(norVecSet))

		for j in range(len(singleTriangleSet)):
			triangleSet.append(singleTriangleSet[j])
			triNormVecs.append(singleNorVecSet[j])

	#normalVectors, triangleSet = subdivisionNew.subdivision(oriTriangleSet,triNormVecs,n)

	forceVecs = np.zeros((len(triNormVecs),3))

	for i in range(len(forceVecs)):
		forceVecs[i] = -1*triNormVecs[i]*3

	Llist, Lmat = LSolver.lengthSolver(triangleSet,triNormVecs,forceVecs)

	positions = Mij.pointsFromSTL(triangleSet)

	Mijmatrix = Mij.MijMat(10,Llist,triangleSet,positions)
	OTMat = otherTermMat.otherTermMat(positions,Mijmatrix)
	Dmat = diagMatrix.Dmat(positions,Mijmatrix)

	BigMatrix = OTMat + Dmat

	listOfLength0 = plotEigenVectorLength(BigMatrix, 0, positions)
	listOfLength1 = plotEigenVectorLength(BigMatrix, 1, positions)
	listOfLength2 = plotEigenVectorLength(BigMatrix, 2, positions)
	listOfLength3 = plotEigenVectorLength(BigMatrix, 3, positions)


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

	w, v = np.linalg.eig(BigMatrix)
	print("eigenvalues = " + str(v))
	
	plt.show()
