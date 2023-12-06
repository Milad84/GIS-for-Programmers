import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt


polygon1_coords = [(0, 0), (0, 2), (2, 2), (2, 0)]
polygon2_coords = [(1, 1), (1, 3), (3, 3), (3, 1)]
polygon3_coords = [(2, 0), (2, 2), (4, 2), (4, 0)]

polygon1 = Polygon(polygon1_coords)
polygon2 = Polygon(polygon2_coords)
polygon3 = Polygon(polygon3_coords)

polygon_data = {'geometry': [polygon1, polygon2, polygon3]}
polygon_gdf = gpd.GeoDataFrame(polygon_data)

erase_polygon_coords = [(1.5, 0.5), (1.5, 2.5), (2.5, 2.5), (2.5, 0.5)]
erase_polygon = Polygon(erase_polygon_coords)    #A

erase_polygon_data = {'geometry': [erase_polygon]}
erase_polygon_gdf = gpd.GeoDataFrame(erase_polygon_data)    #B

erased_layer = gpd.overlay(polygon_gdf, erase_polygon_gdf, how='difference')    #C

fig, ax = plt.subplots()
polygon_gdf.plot(ax=ax, facecolor='blue', edgecolor='black', alpha=0.7)

erase_polygon_gdf.plot(ax=ax, facecolor='red', edgecolor='black', alpha=0.7)

fig, ax = plt.subplots()
erased_layer.plot(ax=ax, facecolor='green', edgecolor='black', alpha=0.7)

ax.set_aspect('equal')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()
#A Create the erase polygon
#B Create a GeoDataFrame from the erase polygon 
#C Perform the erase operation
