import math
import numpy as np
from stl import mesh

import LSolver
import crossArea


def MijMat(elastic,l,triangleSet,positions):

	"""
	Calculating Mij, a matrix of spring constants over length of strings
	Input: elastic = elastic modulus/Young's modulus
		   l = the length calculated by the L solver based on force
		   triangleSet = the entire set of triangles after necessary subdivision
	Output: A matrix of spring constants for each string
	"""

	Mij = np.zeros((len(positions),len(positions)))
	triangleAreaSet = crossArea.triangleArea(triangleSet)

	for i in range(len(positions)):
		for j in range(len(positions)):

			triIndex = sameTriangle(i,j,positions,triangleSet)
			#print(triIndex)

			if i == j:
				Mij[i,j] = 0
			elif len(triIndex) == 0:
				Mij[i,j] = 0
			elif len(triIndex) == 1:
				print("Two points only present in one triangle." + " i = " + str(i) + " j = " + str(j))
			elif len(triIndex) == 2:

				# k needs to be arbitrary. Need to fix that later
				
				k1 = triangleAreaSet[triIndex[0]]*elastic/l[triIndex[0]]
				k2 = triangleAreaSet[triIndex[1]]*elastic/l[triIndex[1]]
				k = (k1+k2)/2
				Mij[i,j] = k/np.linalg.norm(positions[j]-positions[i])

	#print(Mij)
	#print(len(positions))
	#print(len(Mij))
	#print(len(Mij[0]))
	#print(Mij[21])
	
	return Mij


def sameTriangle(indexI,indexJ,positions,triangleSet):

	"""
	Test if two points are in the same triangle

	Input: indexI = the index of the first point in positions
		   indexJ = the index of the second point in positions (indexI has to be different from indexJ)
		   positions = the list of all unique points from the STL file
		   triangleSet = the STL file or the triangle set generated after
	Output: triIndex = a list of 0 to 2 elements, indices of the triangles that contain the two point from input
	"""

	triIndex = []

	if indexI != indexJ:
		for m in range(len(triangleSet)):
			triangleI = -2
			triangleJ = -3
			for n in range(len(triangleSet[m])):
				#print("m = " + str(m))
				#print("n = " + str(n))
				if abs(np.linalg.norm(positions[indexI] - triangleSet[m][n]))<1e-5:
					#print(positions[indexI])
					#print("triangleSet[m][n] = " + str(triangleSet[m][n]))
					triangleI = m
					#print("Triangle I = " + str(triangleI))
				if abs(np.linalg.norm(positions[indexJ] - triangleSet[m][n]))<1e-5:
					#print(positions[indexJ])
					triangleJ = m
					#print("Triangle J = " + str(triangleJ))
			if triangleI == triangleJ:
				triIndex.append(m)

	#print("counter = " + str(counter))
	#print("triangle indices = " + str(triIndex))

	return triIndex



def pointsFromSTL(triangleSet):

	"""
	Decomposing the STL file, creating a new list containing only unique points removing duplicates

	Input: triangleSet = the set of triangles from the STL file
	Output: positions = a list of unique points from the triangleSet without duplicates
	"""

	temp = []

	for triangle in triangleSet:
		temp.append(triangle[0])
		temp.append(triangle[1])
		temp.append(triangle[2])

	positions = [temp[0]]

	for i in range(1, len(temp)):
		if all(abs(np.linalg.norm(temp[i]-element))>1e-5 for element in positions):
			positions.append(temp[i])

	#print("positions = " + str(positions))
	#print(len(positions))

	return positions



#positions = np.array([[1,2,3],[2,3,4],[3,4,5],[7,8,9],[1,5,6]])
#triangleSet = np.array([[[1,2,3],[2,3,4],[7,8,9]],[[1,2,3],[2,3,4],[1,5,6]],[[3,4,5],[1,5,6],[7,8,9]]])

"""
sphere_mesh = mesh.Mesh.from_file('sphere.stl')
triangleSet = sphere_mesh.vectors
triNormVecs = sphere_mesh.normals
forceVecs = np.zeros((len(triangleSet),3))

for i in range(len(forceVecs)):
	forceVecs[i] = -1*triNormVecs[i]*3

l = LSolver.lengthSolver(triangleSet,triNormVecs,forceVecs)

positions = pointsFromSTL(triangleSet)

sameTriangle(0,1,positions,triangleSet)
#sameTriangle(2,3,positions,triangleSet)
#sameTriangle(17,30,positions,triangleSet)
MijMat(10,l,triangleSet,positions)
"""