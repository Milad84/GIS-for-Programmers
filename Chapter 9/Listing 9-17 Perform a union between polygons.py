import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

polygon1_coords = [(0, 0), (0, 2), (2, 2), (2, 0)]    #A
polygon2_coords = [(1, 1), (1, 3), (3, 3), (3, 1)]
polygon3_coords = [(2, 0), (2, 2), (4, 2), (4, 0)]

polygon1 = Polygon(polygon1_coords)
polygon2 = Polygon(polygon2_coords)
polygon3 = Polygon(polygon3_coords)

gdf_polygons = gpd.GeoDataFrame(geometry=[polygon1, polygon2, polygon3])

fig, ax = plt.subplots(figsize=(8, 6))    #B

gdf_polygons.plot(ax=ax, facecolor='none', edgecolor='blue', linewidth=1, label='Polygons')

ax.set_title('Individual Polygons')
plt.show()

union_result = gdf_polygons.unary_union    #C

gdf_union = gpd.GeoDataFrame(geometry=[union_result])    #D

fig, ax = plt.subplots(figsize=(8, 6))

gdf_polygons.plot(ax=ax, facecolor='none', edgecolor='blue', linewidth=1, label='Polygons')    #E

gdf_union.plot(ax=ax, facecolor='yellow', edgecolor='red', linewidth=2, label='Union')    #F

ax.set_title('Union Result')

plt.show()
#A Create polygons
#B Visualize the individual polygons
#C Perform the union operation
#D Create a GeoDataFrame with the union result
#E Plot the polygons in blue
#F Plot the union result in yellow
