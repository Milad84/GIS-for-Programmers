from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

ds = gdal.Open(r"D:\LC08_L1TP_023031_20230511_20230518_02_T1_B1.tif")
array = ds.GetRasterBand(1).ReadAsArray()
plt.imshow(array)
plt.colorbar()
print(ds.GetGeoTransform())
print (ds.GetProjection())

