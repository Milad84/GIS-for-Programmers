
import geopandas as gpd
import osmnx as ox
from shapely.geometry import Point, MultiPoint
import matplotlib.pyplot as plt
import random

north, south, east, west = 40.9, 40.6, -73.8, -74.1    #A

G = ox.graph_from_bbox(north, south, east, west, network_type='drive', simplify=True)    #B

nodes, edges = ox.graph_to_gdfs(G)    #C

crash_points = [Point(random.uniform(west, east), random.uniform(south, north)) for _ in range(50)]    #D
crash_data = gpd.GeoDataFrame(geometry=crash_points)

nearest_edges = []    #E
for point in crash_points:
    distances = edges['geometry'].apply(lambda geom: geom.distance(point))
    nearest_edge = edges.loc[distances.idxmin()]
    nearest_edges.append(nearest_edge)

nearest_edges_gdf = gpd.GeoDataFrame(nearest_edges)    #F

fig, ax = plt.subplots(figsize=(10, 10))    #G
edges.plot(ax=ax, linewidth=1, edgecolor='black', linestyle='-', label='Street Network')
crash_data.plot(ax=ax, color='red', markersize=20, label='Crash Points', zorder=2)
nearest_edges_gdf.plot(ax=ax, color='blue', markersize=10, label='Nearest Edges')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

plt.title('Street Network and Crash Points')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

#A Set up the bounding box coordinates for your area of interest
#B Retrieve the street network within the bounding box
#C Extract the nodes and edges from the street network
#D Generate random crash points
#E Find the nearest edge for each crash point
#F Create a GeoDataFrame of the nearest edges to the crash points
#G Visualize the street network and crash points

