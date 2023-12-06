import rasterio
import numpy as np

with rasterio.open('raster1.tif') as src1, rasterio.open('raster2.tif') as src2:
    
    if src1.crs != src2.crs:    #A
        src2 = src2.to_crs(src1.crs)
    if src1.transform != src2.transform or src1.width != src2.width or    src1.height != src2.height:    #B
        data2 = np.empty((src1.count, src1.height, src1.width), dtype=src1.dtypes[0])
        rasterio.warp.reproject(src2.read(), data2, src_transform=src2.transform, src_crs=src2.crs,
                                dst_transform=src1.transform, dst_crs=src1.crs, resampling=rasterio.enums.Resampling.bilinear)
    else:
        data2 = src2.read()

stacked_data = np.concatenate([src1.read(), data2], axis=0)    #C

red_band = stacked_data[3]    #D  
nir_band = stacked_data[4]    #E 

ndvi = (nir_band - red_band) / (nir_band + red_band)

threshold = 0.2    #F 
change_map = np.where(ndvi > threshold, 1, 0)


import matplotlib.pyplot as plt
 
plt.imshow(ndvi[0], cmap='RdYlGn')    #G
plt.colorbar(label='NDVI')
plt.title('NDVI for Time Period 1')
plt.show()

plt.imshow(change_map, cmap='binary')    #H
plt.title('Forest Change Map')
plt.show()
#A Reproject if needed
#B Resample and align if needed
#C Stack the raster data
#D Compute vegetation index assuming the red band is at index 3
#E Compute vegetation index assuming the NIR band is at index 4
#F Change detection analysis by using a thresholding approach
#G Plotting the NDVI for the first period
#H Plot the change map
