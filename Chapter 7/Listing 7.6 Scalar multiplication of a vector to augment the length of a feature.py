import numpy as np
import matplotlib.pyplot as plt

vector = np.array([3, 4])    #A
scalar = 2    #B
result = scalar * vector    #C

plt.figure(figsize=(6, 6))

plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original Vector')    #D


plt.quiver(0, 0, result[0], result[1], angles='xy', scale_units='xy', scale=1, color='red', label='Scaled Vector')    #E

plt.xlim(-1, 7)    #F
plt.ylim(-1, 9)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scalar Multiplication of a Vector')

plt.legend()
plt.show()
#A Define a vector as a NumPy array
#B Define a scalar value
#C Perform scalar multiplication
#D Plot the original vector
#E Plot the resulting vector after scalar multiplication
#F Set the limits of the plot


