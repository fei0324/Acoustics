import math
import numpy as np
from stl import mesh

def rotationMat(n):

	"""
	Create a transformation matrix rotate the triangle plane to the xy plane
	Preparation for checking if point is inside of a triangle
	Step after translation t: (x,y,z) -> (x,y,z-d/c)
	Input: n = the normal vector of the triangle plane
	Output: rotation matrix
	"""
	cosAngle = n[2]/np.linalg.norm(n)
	sinAngle = np.sin(np.arccos(cosAngle))

	u = np.array([n[1],-1*n[0],0])/np.linalg.norm(n)
	rotMat = np.zeros((3,3))
	rotMat[0] = [cosAngle+u[0]**2*(1-cosAngle),u[0]*u[1]*(1-cosAngle),u[1]*sinAngle]
	rotMat[1] = [u[0]*u[1]*(1-cosAngle),cosAngle+u[1]**2*(1-cosAngle),-1*u[0]*sinAngle]
	rotMat[2] = [-1*u[1]*sinAngle,u[0]*sinAngle,cosAngle]

	return rotMat


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

				# Transform the intersection point and vertices of the triangle
				rotMat = rotationMat(triNormVecs[j])
				d = np.dot(triNormVecs[j], p[j])
				pt1 = triangles[j][0]
				pt2 = triangles[j][1]
				pt3 = triangles[j][2] + d/triNormVecs[j][2]
				intersectPoint[2] = intersectPoint[2] + d/triNormVecs[j][2]

				newPt1 = np.dot(rotMat,pt1)
				newPt2 = np.dot(rotMat,pt2)
				newPt3 - np.dot(rotMat,pt3)
				newIntersect = np.dot(rotMat,intersectPoint)

				# Verify if the point is inside of the triangle
				a = [[(newPt2-newPt1)[0],(newPt3-newPt1)[0]],[(newPt2-newPt1)[1],(newPt3-newPt1)[1]]]
				b = [(newIntersect-newPt1)[0],(newIntersect-newPt1)[1]]
				x = np.linalg.solve(a,b)

				if 0<=x[0]<=1 and 0<=x[1]<=1:
					L = t*forceVecs[i]
	return L


# read an stl file
sphere_mesh = mesh.Mesh.from_file('sphere.stl')
triNormVecs = sphere_mesh.normals
triangles = sphere_mesh.vectors

#LSolver(triangles, triNormVecs, [[0,0,0],[1,1,1]])