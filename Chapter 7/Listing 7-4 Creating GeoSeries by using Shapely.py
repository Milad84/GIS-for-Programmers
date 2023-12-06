import pandas as pd
import shapely.geometry
import shapely.wkt
import geopandas as gpd
import matplotlib.pyplot as plt

pol1 = shapely.wkt.loads('POLYGON ((0 0, 0 -1, 7.5 -1, 7.5 0, 0 0))')
pol2 = shapely.wkt.loads('POLYGON ((0 1, 1 0, 2 0.5, 3 0, 4 0, 5 0.5, 6 -0.5, 7 -0.5, 7 1, 0 1))')

s = gpd.GeoSeries([pol1, pol2], crs=4326)
d = {'name': ['a', 'b'], 'geometry': s}

gdf = gpd.GeoDataFrame(d)

print(gdf)
gdf.plot(color="none", edgecolor="red");

plt.show()
