import rasterio
import numpy as np
import matplotlib.pyplot as plt

with rasterio.open('land_surface_temperature.tif') as lst_src:
    lst_data = lst_src.read(1)    #A

with rasterio.open('land_use.tif') as lu_src:
    lu_data = lu_src.read(1)

assert lst_src.shape == lu_src.shape, "Raster shapes do not match!"    #B

urban_areas = np.logical_or(lu_data == 1, lu_data == 2)    #C
uhi_intensity = np.zeros_like(lst_data)

uhi_intensity[urban_areas] = lst_data[urban_areas] - np.mean(lst_data[~urban_areas])    #D

plt.figure(figsize=(10, 8))
plt.imshow(uhi_intensity, cmap='hot', vmin=0, vmax=10)  
plt.colorbar(label='Urban Heat Island Intensity (°C)')
plt.title('Urban Heat Island Intensity')
plt.xlabel('Pixel Column')
plt.ylabel('Pixel Row')
plt.show()
#A Load the raster files
#B Ensure both rasters have the same shape and extent
#C Combine the raster layers and assume land use categories 1 and 2 represent urban areas 
#D Calculate UHI intensity as the difference between urban and non-urban temperatures
