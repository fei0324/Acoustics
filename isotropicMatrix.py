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
	k = 2*pi/wavelength

	distance = np.zeros(len(samplePoints),len(sourcePoints))
	# Currently based on the questionable indices order: x.shape = (depth, row, column)
	# i for row, j for column, k for depth
	for i in range(1, len(samplePoints.shape[1])):
		for j in range(1, len(sourcePoints.shape[2])):
			for k in range(1, len(samplePoints.shape[0])):

				distance += (samplePoints[k][i][0] - sourcePoints[k][0][j])**2
				#skeptical...


	distance = math.sqrt(distance)

	mat = math.e**(1j*k*distance)/(4*math.pi*distance)

	return mat
