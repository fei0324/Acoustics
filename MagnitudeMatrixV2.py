import numpy as np
"""
	goal: to make a matrix that outputs the magnitudes of distance between three point arrays 
	input: a Nx3 matrix of coordinates of points
	output: a NXN matrix of the magnitudes of distance between these points
	notes: still needs to incorporate the spring constants to make a Mij matrix of constants but this program is just the magnitudes in a matrix
"""


def MoM (pterm):
	#n is the number of p terms we have dim is the dimensions

	dim, n = pterm.shape
	n = n + 1 
	m = np.zeros((n,n))
	for i in range(0,n):
		a = pterms[[i],:]
		#a = pterms[i]
		for j in range(0,n):
			b = pterms[[j],:]  
			#b = pterms[j]  
			c = np.sqrt(np.sum(np.square(a - b)))
			m[i][j] = c
	return m 

def magnitudeMatrix(points):

	magMatrix = np.zeros((len(points),len(points)))

	for i in range(len(points)):
		for j in range(len(points)):
			magMatrix[i][j] = np.linalg.norm(points[i]-points[j])
	print("magnitudes = " + str(magMatrix))

# arbitrary inputs for test
pterms = np.matrix([[0,0,1],[3,2,3],[1,1,1],[5,6,8]])

print MoM(pterms)
magnitudeMatrix(pterms)
