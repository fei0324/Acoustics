import math
import numpy as np
from stl import mesh

from subdivision import *


def triangleArea(triangleSet):

	"""
	Calculate areas of subdivided triangles

	Input: the set of subdivided triangles

	Output: a list of the areas with corresponding idices with the the triangleSet
	"""

	triangleAreaSet = []

	for i in range(len(triangleSet)):
		v1 = triangleSet[i][1] - triangleSet[i][0]
		v2 = triangleSet[i][2] - triangleSet[i][0]
		area = np.linalg.norm(np.cross(v1, v2))/2
		triangleAreaSet.append(area)

	return triangleAreaSet

def crossArea(forceVecs,triangleAreaSet,triNormVecs):

	"""
	Preparation for Young's Modulus
	Calculate the cross sectional areas perpendicular to the force vectors
	Input: forceVecs = a list of force vectors
		   triangleAreaSet = area of triangles
		   triNormVecs = a list of normal vectors for each triangle (should be given by the stl file)
	Output: A list of cross sectional area, approximated by the area of the triangle perpendicular to the force vector
	"""

	crossAreaSet = np.zeros(len(triangleAreaSet))

	for i in range(len(forceVecs)):
		costheta = np.dot(forceVecs[i],triNormVecs[i])/(np.linalg.norm(forceVecs[i])*np.linalg.norm(triNormVecs[i]))
		crossAreaSet[i] = abs(costheta*triangleAreaSet[i])

	return crossAreaSet

sphere_mesh = mesh.Mesh.from_file('sphere.stl')
triNormVecs = sphere_mesh.normals
triangles = sphere_mesh.vectors
#print("triangles = " + str(triangles))
forceVecs = np.zeros((len(triangles),3))
forceVecs[14] = np.array([2,3,1])
triangleAreaSet = triangleArea(triangles)
print(triangleAreaSet)
print(crossArea(forceVecs,triangleAreaSet,triNormVecs))
