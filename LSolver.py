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

	L = []

	# Force vector starting point (approximating with the centroid of the triangle)
	for triangle in triangles:
		p.append(triangle[0])

	# Check if the force vector is parallel to the normal vector of a triangle
	for i in range(len(forceVecs)):
		for j in range(len(triNormVecs)):
			if np.dot(forceVecs[i], triNormVecs[j]) != 0.:

				# Find intersection point on each plane
				numer = np.dot(triNormVecs[j],(p[j]-p[i]))
				denom = np.dot(triNormVecs[j],forceVecs[i])
				t = numer/denom
				intersectPoint = p[i] + t*forceVecs[i]

				# Verify if the point is inside of the triangle

				e1 = triangles[j][1] - triangles[j][0]
				e2 = triangles[j][2] - triangles[j][0]
				v = intersectPoint - triangles[j][0]

				a = np.transpose(np.array([e1,e2]))

				x = np.linalg.lstsq(a,v)[0]

				if i == 80:
					print("force = " + str(forceVecs[i]))
					print("j = " + str(j))
					print(x)
					print("t = " + str(t))

				if 0 <= x[0] <= 1 and 0 <= x[1] <= 1 and 0 <= x[0]+x[1] <= 1:
					l = np.linalg.norm(t*forceVecs[i])

					#if i == 80:
					#	print("force = " + str(forceVecs[i]))
					#	print("j = " + str(j))
					#	print(x)
					#	print("t = " + str(t))
					if abs(l-0.)>1e-10:

						#print("i = " + str(i))
						#print("j = " + str(j))
						#print("t = " + str(t))
						#print("numer = " + str(numer))
						#print("p[i] = " + str(p[i]) + " p[j] = " + str(p[j]))
						#print("denom = " + str(denom))
						L.append(l)
						break
	print(len(L))
						
						
	return L


# read an stl file
cylinder_mesh = mesh.Mesh.from_file('cylinder.stl')
triNormVecs = cylinder_mesh.normals
triangles = cylinder_mesh.vectors
print("triangles = " + str(triangles))
forceVecs = np.zeros((len(triangles),3))
for i in range(len(forceVecs)):
	forceVecs[i] = -1*triNormVecs[i]*35

#rotationMat([0,1,0])
#rotationMat([2,3,4])
#print("force = " + str(forceVecs))
print("number of triangles = " + str(len(triangles)))
print(LSolver(triangles, triNormVecs, forceVecs))