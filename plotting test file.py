import matplotlib.pyplot as plt 
import isotropicMatrix as Imat
import numpy as np
import math
points = np.linspace(1,50,50)
print points
a = Imat.isotropicMatrix(10, points, np.array([0]))
b = np.squeeze(np.asarray(a))
print "this is b"
print b
c = b*-1j
plt.figure(1)
plt.subplot(211)
plt.plot(points, b, 'bo')

plt.subplot(212)
plt.plot(points, c, 'r--')
plt.show()