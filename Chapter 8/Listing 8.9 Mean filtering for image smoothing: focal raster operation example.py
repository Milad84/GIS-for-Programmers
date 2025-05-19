import numpy as np
from scipy.signal import convolve2d

image = np.array([[10, 20, 30, 40, 50],    #A
                  [15, 25, 35, 45, 55],
                  [12, 22, 32, 42, 52],
                  [18, 28, 38, 48, 58],
                  [14, 24, 34, 44, 54]])

mean_filter = np.array([[1, 1, 1],    #B
                        [1, 1, 1],
                        [1, 1, 1]])

filtered_image = convolve2d(image, mean_filter, mode='same', boundary='wrap') / 9    #C

print("Original Image:")
print(image)
print("\nFiltered Image:")
print(filtered_image.round().astype(int))
#A Sample grayscale image represented as a 2D array
#B Define the mean filter kernel (3x3)
#C Apply the mean filter using convolution
