import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([1, 2, 3])    #A
B = np.array([4, 5, 6])
C = np.array([2, 7, 4])

AB = B – A    #B
AC = C - A

normal_vector = np.cross(AB, AC)    #C

fig = plt.figure()    #D
ax = fig.add_subplot(111, projection='3d')

ax.scatter(A[0], A[1], A[2], color='red', label='A')    #E
ax.scatter(B[0], B[1], B[2], color='green', label='B')
ax.scatter(C[0], C[1], C[2], color='blue', label='C')

ax.quiver(A[0], A[1], A[2], AB[0], AB[1], AB[2], color='orange', label='AB Vector')    #F
ax.quiver(A[0], A[1], A[2], AC[0], AC[1], AC[2], color='purple', label='AC Vector')

normal_vector_scaled = normal_vector * 0.3    #G
ax.quiver(A[0], A[1], A[2], normal_vector_scaled[0],    normal_vector_scaled[1], normal_vector_scaled[2], color='black', label='Normal Vector')    #H

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
#A Define the three vertices of the building
#B Calculate the vectors AB and AC
#C Calculate the cross-product to find the normal vector of the roof surface
#D Create a 3D plot for visualization
#E Plot the building vertices
#F Plot the roof edges AB and AC 
#G Scale the normal vector for better visualization
#H Plot the normal vector as the cross product of AB and AC

