import numpy as np
import matplotlib.pyplot as plt

vector1 = np.array([2, 3])    #A
vector2 = np.array([4, 5])

dot_product = np.dot(vector1, vector2)    #B

plt.figure()

plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector 1')
plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector 2')

plt.xlim(-1, 5)    #C
plt.ylim(-1, 6)

plt.grid(True)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Visualization of Vectors')

plt.legend()    #D

alignment = "Parallel" if dot_product == np.linalg.norm(vector1) * np.linalg.norm(vector2) else "Not Parallel"    #E
alignment_text = f"Alignment: {alignment}\nDot Product: {dot_product}"

plt.text(0.5, 5.5, alignment_text, fontsize=10, ha='center', va='center')
plt.show()
#A Define two vectors as NumPy arrays
#B Calculate the dot product
#C Set the limits of the plot
#D Add a legend
#E Calculate alignment based on the dot product
