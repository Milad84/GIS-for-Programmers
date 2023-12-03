import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

polygon1_coords = [(0, 0), (0, 2), (2, 2), (2, 0)]
polygon1 = Polygon(polygon1_coords)

polygon2_coords = [(1, 1), (1, 3), (3, 3), (3, 1)]
polygon2 = Polygon(polygon2_coords)

polygon1_gdf = gpd.GeoDataFrame(geometry=[polygon1])
polygon2_gdf = gpd.GeoDataFrame(geometry=[polygon2])

clipped_area = gpd.clip(polygon1_gdf, polygon2_gdf)


fig, ax = plt.subplots()
polygon1_gdf.plot(ax=ax, facecolor='none', edgecolor='blue', linewidth=0.8)

polygon2_gdf.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=0.8)

clipped_area.plot(ax=ax, facecolor='green', edgecolor='black', alpha=0.7)

ax.set_aspect('equal')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()
