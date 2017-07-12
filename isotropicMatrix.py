import math
import numpy as np


def isotropicMatrix(wavelength, sourcePoints, samplePoints):

	"""
	Compute the field induced by a collection of isotropic radiators
	
	Input: wavelength = operating wavelength (meters)x0
		   sourcePoints = location of point sources to solve (PxD, meters)
		   samplePoints = location of point where field is desired (SxD, meters)
	Output: matrix that converts sources into samples(SxP)

	"""

	# Wavenumber
	k = 2*math.pi/wavelength

	distance = np.zeros((len(samplePoints),len(sourcePoints)))
	isoMat = np.zeros((len(samplePoints), len(sourcePoints)), dtype=complex)

	# i for row, j for column
	for i in range(0, len(samplePoints)):
		for j in range(0, len(sourcePoints)):
			distance[i,j] = np.linalg.norm(sourcePoints[j]-samplePoints[i])
			isoMat[i,j] = np.exp(-1j*k*distance[i,j])/(4*math.pi*distance[i,j])
	print isoMat

	return isoMat

isotropicMatrix(1, np.array([[10,20,30], [1,2,4], [6,3,6]]), np.array([10,2,4]))
isotropicMatrix(10, np.array([[0,3,4],[0,0,2]]), np.array([0,0,0]))
