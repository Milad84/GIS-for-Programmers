import numpy as np
from PIL import Image

def detect_water(image_path):
    image = Image.open(image_path)    #A
    image_array = np.array(image)

    grayscale_image = image.convert('L')    #B
    grayscale_array = np.array(grayscale_image)

    water_threshold = 120    #C  
    water_mask = np.where(grayscale_array < water_threshold, 1, 0)    #D

    water = np.sum(water_mask)

    return water

image_path = "D:\LC09_L1TP_023031_20230503_20230503_02_T1_refl.tif"
pixel = detect_water(image_path)
print("Estimated water pixels:", pixel)
#A Load the satellite picture
#B Convert the image to grayscale
#C Define thresholds for water detection. Adjust this value to suit your needs.
#D Create a binary mask for water pixels
#E Calculate the water pixels
