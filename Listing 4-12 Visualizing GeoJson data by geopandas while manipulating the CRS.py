import geopandas as gpd
from pyproj import CRS
import matplotlib.pyplot as plt

fp = r'E:\PointsInChad.geojson'    #A
geodata = gpd.read_file(fp, driver='GeoJSON')

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))    #B

lat = 0    #C
lon = 0    #C

wgs84 = CRS.from_proj4("+proj=longlat +datum=WGS84 +no_defs +type=crs".format(lat, lon))

geodataor = geodata.to_crs(wgs84)    #D
world = world.to_crs(wgs84)    #D
base = world.plot(facecolor="none", edgecolor="black", figsize=(12,6))
geodata.plot(ax=base, marker='*', color='green', markersize=5);
plt.show()
#A Layer saved on your machine
#B Create a world layer as a basemap using a layer hosted on a remote server
#C The origin of the CRS
#D Reproject to the desired CRS
