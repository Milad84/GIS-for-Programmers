import numpy as np
import rasterio
from rasterio.plot import show
from scipy import ndimage

file_path = 'D:\LC08_L1TP_023031_20230511_20230518_02_T1\LC08_L1TP_023031_20230511_20230518_02_T1_B1.tif'    #A
with rasterio.open(file_path) as src:
    band1 = src.read(1)


smoothed_band = ndimage.gaussian_filter(band1, sigma=1)    #B

local_mean = ndimage.uniform_filter(band1, size=5)    #C

local_std = np.sqrt(ndimage.uniform_filter((band1 - local_mean)**2, size=5))    #D

threshold = 100    #E  
binary_mask = np.where(band1 > threshold, 1, 0)

show(band1, title="Original Band")
show(smoothed_band, title="Smoothed Band")

show(local_mean, title="Local Mean")
show(local_std, title="Local Standard Deviation")

show(binary_mask, cmap='binary', title="Binary Mask")
#A Read the single-band TIFF file
#B Filtering: Apply Gaussian filter for noise reduction
#C Local Mean: Calculate the local mean using a uniform filter
#D Local Standard Deviation: Calculate the local standard deviation
#E Thresholding: Create a binary mask based on a threshold value. Adjust as needed
