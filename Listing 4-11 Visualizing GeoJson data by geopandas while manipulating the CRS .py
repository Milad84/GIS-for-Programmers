import geopandas as gpd
from pyproj import CRS
import matplotlib.pyplot as plt

# reading data
fp = r'E:\PointsInChad.geojson'
geodata = gpd.read_file(fp, driver='GeoJSON')

# create world layer
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# define center of CRS
lat = 0
lon = 0

wgs84 = CRS.from_proj4("+proj=longlat +datum=WGS84 +no_defs +type=crs".format(lat, lon))

# Re-project and plot
geodataor = geodata.to_crs(wgs84)
world = world.to_crs(wgs84)
base = world.plot(facecolor="none", edgecolor="black", figsize=(12,6))
geodata.plot(ax=base, marker='*', color='green', markersize=5);
plt.show()