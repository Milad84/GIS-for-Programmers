import numpy as np

vector1 = np.array([2, 3])
vector2 = np.array([4, 6])

dot_product = np.dot(vector1, vector2)

magnitude_product = np.linalg.norm(vector1) * np.linalg.norm(vector2)    #A
print("Dot Product:", dot_product)
print("Product of Magnitudes:", magnitude_product)
#A Calculate the product of the magnitudes
