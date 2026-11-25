import matplotlib.pyplot as plt
from scipy.datasets import face 

img = face()
plt.imshow(img)
plt.show()
print (img.shape)

