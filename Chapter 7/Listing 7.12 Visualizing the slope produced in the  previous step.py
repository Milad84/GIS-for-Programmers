from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

slope_path = "D:/slope.tif"    #A
dataset = gdal.Open(slope_path)
band = dataset.GetRasterBand(1)
slope_array = band.ReadAsArray()

cmap = 'RdYlBu'    #B

min_slope = np.min(slope_array)    #C
max_slope = np.max(slope_array)

fig, ax = plt.subplots()    #D

im = ax.imshow(slope_array, cmap=cmap, vmin=min_slope, vmax=max_slope)
cbar = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.04)

ax.set_title("Slope")
ax.set_xlabel("Column")
ax.set_ylabel("Row")
cbar.set_label("Slope")

plt.show()

band = None
dataset = None
#A Read the slope.tif raster
#B Define the color ramp for the slope values
#C Get the minimum and maximum slope values
#D Plot the slope raster

