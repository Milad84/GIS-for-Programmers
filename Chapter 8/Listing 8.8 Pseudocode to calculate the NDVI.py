import rasterio
import numpy as np
import matplotlib.pyplot as plt

nir_band_path = 'nir_band.tif'  
red_band_path = 'red_band.tif'  

with rasterio.open(nir_band_path) as src:
    nir_band = src.read(1)   #A

with rasterio.open(red_band_path) as src:
    red_band = src.read(1)   #A

ndvi = (nir_band - red_band) / (nir_band + red_band)    #B

plt.figure(figsize=(10, 8))
plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
plt.colorbar(label='NDVI')
plt.title('Normalized Difference Vegetation Index (NDVI)')
plt.axis('off')
plt.show()
#A Read the NIR and red bands from the satellite imagery. Replace with your file path.
#B Calculate NDVI.
