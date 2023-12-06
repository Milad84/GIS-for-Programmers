import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt


input_coords = [    #A
    [(0, 0), (0, 4), (4, 4), (4, 0)],
    [(1, 1), (1, 3), (3, 3), (3, 1)],
    [(2, 2), (2, 6), (6, 6), (6, 2)]
]
input_layer = gpd.GeoDataFrame(geometry=[Polygon(coords) for coords in input_coords])

boundary_coords = [    #B
    [(0.5, 1), (0.5, 3), (2.5, 3), (2.5, 1)]
]
boundary_layer = gpd.GeoDataFrame(geometry=[Polygon(coords) for coords in boundary_coords])

split_results = gpd.overlay(input_layer, boundary_layer)    #C

colors = ['green', 'orange', 'purple']    #D

fig, ax = plt.subplots(figsize=(8, 8)) #E

input_layer.plot(ax=ax, facecolor='blue', edgecolor='black', alpha=0.7, label='Input Layer')

boundary_layer.plot(ax=ax, facecolor='red', edgecolor='black', alpha=0.7, label='Boundary Layer')

for i, result in enumerate(split_results.geometry):
    split_color = colors[i % len(colors)]
    gpd.GeoDataFrame(geometry=[result]).plot(ax=ax, facecolor=split_color, edgecolor='black', alpha=0.7, label=f'Split {i+1}')

ax.set_aspect('equal')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

ax.legend()

plt.show()
#A Create the input layer
#B Create the boundary layer (polygon defining the split)
#C Perform the split operation
#D Define colors for each split result polygon
#E Plot the input layer, boundary layer, and split results
