import math
import numpy as np
from isotropicMatrix import *

def boundaryElement(wavelength,sourcePoints,dirichletPoints,desiredFields,neumannPoints,neumannNormals,desiredDerivs):

	"""
	Construct a solution for the scalar Helmholtz equation with mixed Dirichlet-Neumann 
	boundary conditions using the boundary element method

	Input: wavelength      = operating wavelength (meters)
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
		#