import geopandas as gpd
import rasterio
import rasterio.plot as rio_plot
import matplotlib.pyplot as plt
from rasterio.mask import mask
from shapely.geometry import Polygon

raster_file = 'D:\LC08_L1TP_023031_20230511_20230518_02_T1_B1.tif'    #A
src = rasterio.open(raster_file)

left, bottom, right, top = src.bounds    #B

center_x = (left + right) / 2    #C
center_y = (bottom + top) / 2

polygon_size = min((right - left) / 10, (top - bottom) / 10)    #D

minx = center_x - polygon_size / 2    #E
maxx = center_x + polygon_size / 2
miny = center_y - polygon_size / 2
maxy = center_y + polygon_size / 2
polygon = Polygon([(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny)])

mask_gdf = gpd.GeoDataFrame({'geometry': [polygon]}, crs=src.crs)    #F

out_image, out_transform = mask(src, mask_gdf.geometry, crop=True)    #G

out_meta = src.meta.copy()    #H
out_meta.update({
    "driver": "GTiff",
    "height": out_image.shape[1],
    "width": out_image.shape[2],
    "transform": out_transform
})

clipped_raster_file = 'D:\clipped_raster.tif'    #I
with rasterio.open(clipped_raster_file, "w", **out_meta) as dest:
    dest.write(out_image)

#A Load the raster data in TIF format
#B Calculate the bounding box of the raster
#C Calculate the center of the raster
#D Define the size of the smaller polygon to be used as the mask (one-tenth of the original raster)
#E Create the smaller mask polygon at the center of the raster
#F Convert the polygon to a GeoDataFrame
#G Clip the raster based on the mask polygon 
#H Update the metadata of the clipped raster
#I Save the clipped raster to a new TIF file
