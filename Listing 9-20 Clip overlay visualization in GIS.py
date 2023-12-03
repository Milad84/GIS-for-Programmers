import geopandas as gpd
import matplotlib.pyplot as plt

polygon_layer = gpd.read_file('path/to/polygon_layer.shp')    #A

target_layer = gpd.read_file('path/to/target_layer.shp')    #B

clipped_layer = gpd.clip(target_layer, polygon_layer)    #C

fig, ax = plt.subplots()    #D
polygon_layer.plot(ax=ax, facecolor='none', edgecolor='blue', linewidth=0.8)

clipped_layer.plot(ax=ax, facecolor='red',    #E 
edgecolor='black', alpha=0.7)

ax.set_aspect('equal')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()
#A Load the polygon layer
#B Load the target layer to be clipped
#C Perform the clip operation
#D Plot the original layer
#E Plot the clipped layer
