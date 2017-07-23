import math
import numpy as np
from stl import mesh

def LSolver(triangles,triNormVecs,forceVecs):

	"""
	Preparation for Young's Modulus:
		Find the intersection of the extension of the force
		and a triangle on the other side of the object.
		Compute the distance.
	Input: triangles = triangle vectors from the input stl file
		   triNormVecs = normal vectors for each triangle from the stl file
		   forceVecs = a list of force vectors on every triangle
	Output: The length of L for Young's Modulus
	"""

	# Force vector starting point and point on a triangle plane (approximate with the first point of a triangle)
	p = []
	for triangle in triangles:
		p.append(triangle[0])

	# Check if the force vector is parallel to the normal vector of a triangle
	for i in range(len(forceVecs)):
		for j in range(len(triNormVecs)):
			if np.dot(forceVecs[i], triNormVecs[j]) != 0:

				# Find intersection point on each plane
				numer = np.dot(triNormVecs[j],(p[j]-p[i]))
				denom = np.dot(triNormVecs[j],forceVecs[i])
				t = numer/denom
				intersectPoint = p[i] + t*forceVecs[i]

				# Verify if the point is inside of the triangle
				




# read an stl file
sphere_mesh = mesh.Mesh.from_file('sphere.stl')
triNormVecs = sphere_mesh.normals
triangles = sphere_mesh.vectors

LSolver(triangles, triNormVecs, [0,0,0])