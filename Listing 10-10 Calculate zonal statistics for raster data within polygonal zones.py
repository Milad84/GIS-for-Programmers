import rasterio
import geopandas as gpd
from rasterio.features import geometry_mask
from rasterstats import zonal_stats
import numpy as np

raster_path = "path_to_your_raster_file.tif"    #A
raster = rasterio.open(raster_path)

vector_path = "path_to_your_polygon_shapefile.shp"    #B
vector = gpd.read_file(vector_path)

masked_raster, transform = rasterio.mask.mask(raster, vector.geometry, crop=True)    #C

stats = zonal_stats(vector, masked_raster, affine=transform, stats=['mean', 'median', 'sum', 'std', 'min', 'max'])    #D

vector['mean'] = [s['mean'] if s['mean'] is not None else np.nan for s in stats]    #E
vector['median'] = [s['median'] if s['median'] is not None else np.nan for s in stats]
vector['sum'] = [s['sum'] if s['sum'] is not None else np.nan for s in stats]
vector['std'] = [s['std'] if s['std'] is not None else np.nan for s in stats]
vector['min'] = [s['min'] if s['min'] is not None else np.nan for s in stats]
vector['max'] = [s['max'] if s['max'] is not None else np.nan for s in stats]


print(vector)    #F
#vector.to_file("path_to_output_shapefile_with_stats.shp")
#A Load the raster file
#B Load the vector (polygon) file
#C Mask the raster within the polygons
#D Calculate zonal statistics using rasterstats
#E Add the zonal statistics to the GeoDataFrame
#F Print or save the GeoDataFrame with zonal statistics
