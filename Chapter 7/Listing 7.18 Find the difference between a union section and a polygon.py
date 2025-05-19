import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

polygon1_coords = [(0, 0), (0, 2), (2, 2), (2, 0)]
polygon2_coords = [(1, 1), (1, 3), (3, 3), (3, 1)]
polygon3_coords = [(2, 0), (2, 2), (4, 2), (4, 0)]

polygon1 = Polygon(polygon1_coords)
polygon2 = Polygon(polygon2_coords)
polygon3 = Polygon(polygon3_coords)

gdf_polygons = gpd.GeoDataFrame(geometry=[polygon1, polygon2, polygon3])

fig, ax = plt.subplots(figsize=(8, 6))

gdf_polygons.plot(ax=ax, facecolor='none', edgecolor='blue', linewidth=1, label='Polygons')

ax.set_title('Individual Polygons')

plt.show()

union_result = gdf_polygons.unary_union    #A

gdf_union = gpd.GeoDataFrame(geometry=[union_result])

difference_result = gdf_union.difference(gdf_polygons.geometry)    #B

gdf_difference = gpd.GeoDataFrame(geometry=difference_result)    #C

fig, ax = plt.subplots(figsize=(8, 6))    #D

gdf_polygons.plot(ax=ax, facecolor='none', edgecolor='blue', linewidth=1, label='Polygons')

gdf_difference.plot(ax=ax, facecolor='yellow', edgecolor='red', linewidth=2, label='Difference')    #E

ax.set_title('Difference Result')

plt.show()
#A Perform the union operation
#B Perform the difference operation
#C Create a GeoDataFrame with the difference result
#D Visualize the difference result
#E Plot the difference result in yellow
