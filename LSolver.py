import math
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt

def lengthSolver(triangles,triNormVecs,forceVecs):

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

	u = np.zeros((len(triangles),3))
	v = np.zeros((len(triangles),3))
	centroid = np.zeros((len(triangles),3))
	Lmat = np.zeros((len(triangles),len(triangles)))
	Llist = np.zeros(len(triangles))
	#Xmat = np.zeros((len(triangles),len(triangles)))

	# Vector u, vector v and force vector starting point (approximating with the centroid of triangles)
	for i in range(len(triangles)):
		u[i] = triangles[i][1] - triangles[i][0]
		v[i] = triangles[i][2] - triangles[i][0]
		centroid[i] = triangles[i][0] + (1/3)*u[i] + (1/3)*v[i]

	for i in range(len(forceVecs)):
		for j in range(len(triNormVecs)):

			# If the force vector is parallel to the triangle plane, assign -10
			if abs(np.dot(forceVecs[i], triNormVecs[j])-0.)<1e-05:
				Lmat[i,j] = -10
				#Xmat[i,j] = -10
			
			else:
				# Find intersection point on the plane
				numer = np.dot(triNormVecs[j],triangles[j][0]-centroid[i])
				denom = np.dot(triNormVecs[j],forceVecs[i])
				t = numer/denom
				intersectPoint = centroid[i] + t*forceVecs[i]

				# Verify if the point is in the triangle
				q = intersectPoint - triangles[j][0]

				a = np.transpose(np.array([u[j],v[j]]))

				#x = np.linalg.solve(a,q)
				x = np.linalg.lstsq(a,q)[0]
				#Xmat[i,j] = x

				if -1e-05<=x[0]<=1+1e-05 and -1e-05<=x[1]<=1+1e-05 and -1e-05<=x[0]+x[1]<=1+1e-05:
					l = np.linalg.norm(intersectPoint - centroid[i])
					Lmat[i,j] = l

				# If the intersection point if outside of the triangle, assign -20
				else:
					Lmat[i,j] = -20

	for i in range(len(triangles)):
		Llist[i] = max(Lmat[i])
	#print(Xmat)
	#print(len(Lmat))
	#print(len(Lmat[0]))
	#print(Llist)
	#print("L list = " + str(Llist))
	#print(Lmat)
	#print(Lmat[0])
	#print(Lmat[2])
	#print(Lmat[3])
	#print(Lmat[4])
	#print(Lmat[5])
	#print(Lmat[25])
	#print(Lmat[90])

	return Llist, Lmat

"""
triangles = np.array([[[0,0,0],[3,0,0],[0,3,0]],[[0,0,4],[3,0,4],[0,3,4]]])
triNormVecs = np.array([[0,0,1],[0,0,1]])

forceVecs = np.array([[0,0,3],[0,0,-3]])

forceVecs = np.array([[1,1,0],[1,1,0]])

forceVecs = np.array([[0,5,5],[0,5,5]])

LSolver(triangles,triNormVecs,forceVecs1)
LSolver(triangles,triNormVecs,forceVecs2)
LSolver(triangles,triNormVecs,forceVecs3)
"""
"""
sphere_mesh = mesh.Mesh.from_file('sphere.stl')
triNormVecs = sphere_mesh.normals
triangles = sphere_mesh.vectors
#print("triangles = " + str(triangles))
forceVecs = np.zeros((len(triangles),3))
for i in range(len(forceVecs)):
	forceVecs[i] = -1*triNormVecs[i]*3

print("number of triangles = " + str(len(triangles)))
"""
"""

cylinder_mesh = mesh.Mesh.from_file('cylinder.stl')
triNormVecs = cylinder_mesh.normals
triangles = cylinder_mesh.vectors
#print("triangles = " + str(triangles))
forceVecs = np.zeros((len(triangles),3))
for i in range(len(forceVecs)):
	forceVecs[i] = -1*triNormVecs[i]*30

print("number of triangles = " + str(len(triangles)))


Llist, Lmat = lengthSolver(triangles, triNormVecs, forceVecs)

plt.figure(1)
imageForL = np.random.rand(len(Lmat), len(Lmat[0]))
plt.imshow(imageForL,cmap=plt.cm.cool)
plt.colorbar()
plt.title("L Matrix")

plt.figure(2)
plt.plot(Llist, 'ro')
plt.title("L list")
plt.show()
"""