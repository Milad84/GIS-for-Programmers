import rasterio
from rasterio.plot import show

fp = r'D:\USGS_1M_13_x49y440_CO_DRCOG_2020_B20.tif'    #A
img = rasterio.open(fp)    #B
show(img)
#A Choosing the file saved in the system
