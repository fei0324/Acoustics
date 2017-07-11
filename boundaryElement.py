import math
import numpy as np
from isotropicMatrix import *

def boundaryElement(wavelength,sourcePoints,dirichletPoints,desiredFields,neumannPoints,neumannNormals,desiredDerivs):

	"""
	Construct a solution for the scalar Helmholtz equation with mixed Dirichlet-Neumann 
	boundary conditions using the boundary element method

	Input: wavelength    = operating wavelength (meters)
	     sourcePoints    = location of point sources to solve (PxD, meters)
	     dirichletPoints = locations of points where the field is specified (IxD, meters)
	     desiredFields   = the values of the field at each Dirichlet point (Ix1, field)
	     neumannPoints   = locations of points where normal derivatives are specified (NxD, meters)
	     neumannNormals  = normal vectors at each Neumann point (NxD, unit vector)
	     desiredDerivs   = the value of the derivative of the field at each Neumann point (Nx1, field/meter)

	Output: sources = values of each source (Px1)
	"""

	# Wavenumber
	k = 2*math.pi/wavelength

	# Dirichlet subproblem
	if dirichletPoints:
		# Construct Dirichlet submatrix via phases (IxP)
		dirichletMat = isotropicMatrix(wavelength,sourcePoints,dirichletPoints)

	# Neumann subproblem
	if neumannPoints:
		# Normalize supplied normal vectors (NxD)
		for i in range(len(neumannNormals)):
			neumannNormals[i] = neumannNormals[i]/np.linalg.norm(neumannNormals[i])

		# Construct vectors from each source point to each Neumann point (NxPxD)
		neumannRangeVector = np.zeros((len(neumannPoints),len(sourcePoints)))
		for i in range(len(neumannPoints)):
			for j in range(len(sourcePoints)):
				neumannRangeVector[i,j] = neumannPoints[i] - sourcePoints[j]

		# Distance source to Neumann points (NxP)
		neumannRange = np.zeros((len(neumannRangeVector[0,:]),len(neumannRangeVector[:,0])))
		for i in range(len(neumannRangeVector[0,:])):
			for j in range(len(neumannRangeVector[:,0])):
				neumannRange[i,j] = np.linalg.norm(neumannRangeVector[i,j])

		# Vector source to Neumann, projected onto local normals (NxP)
		neumannProj = np.zeros((len(neumannRangeVector[0,:]),len(neumannRangeVector[:,0])))
		for i in range(len(neumannRangeVector[0,:])):
			for j in range(len(neumannRangeVector[:,0])):
				neumannProj[i,j] = neumannRangeVector[i,j]*neumannNormals[i]

		# Construct Neumann submatrix (NxP)
		neumannMat = np.zeros((len(neumannRangeVector[0,:]),len(neumannRangeVector[:,0])), dtype=complex)
		for i in range(len(neumannRangeVector[0,:])):
			for j in range(len(neumannRangeVector[:,0])):
				neumannMat[i,j] = np.exp(-1j*k*neumannRange[i,j])/(4*math.pi*neumannRange[i,j]**2)*neumannProj[i,j]*(1-1/neumannRange[i,j])

	if dirichletPoints and neumannPoints:
		# Should construct two new matrices? and do no.linalg.lstsq?
		# same number of columns but different rows? 
		dirNeuMat = np.zeros((len(dirichletMat[0,:])+len(neumannMat[0,:])),len(dirichletMat[:,0]))
		fieDerMat = np.zeros((len(desiredFields[0,:])+len(desiredDerivs[0,:]),len(desiredFields[:,0])))

		for i in range(len(dirichletMat[0,:])):
			for j in range(len(dirichletMat[:,0])):
				dirNeuMat[i,j] = dirichletMat[i,j]

		for i in range(len(neumannMat[0,:])):
			for j in range(len(neumannMat[:,0])):
				dirNeuMat[len(dirichletMat[0,:])+i,j] = neumannMat[i,j]

		for i in range(len(desiredFields[0,:])):
			for j in range(len(desiredFields[:,0])):
				fieDerMat[i,j] = desiredFields[i,j]

		for i in range(len(desiredDerivs[0,:])):
			for j in range(len(desiredDerivs[:,0])):
				fieDerMat[len(desiredFields[0,:])+i,j] = desiredDerivs[i,j]

		sources = np.linalg.lstsq(dirNeuMat,fieDerMat)[0]

	elif dirichletPoints:
		sources = np.linalg.lstsq(dirichletMat,desiredFields)[0]
	elif neumannPoints:
		sources = np.linalg.lstsq(neumannMat,desiredDerivs)[0]

	return sources



