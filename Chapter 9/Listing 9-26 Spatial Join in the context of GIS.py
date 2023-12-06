import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd

points_data = {    #A
    'City': ['City A', 'City B', 'City C'],
    'Population': [1000000, 500000, 800000],
    'geometry': [Point(1, 1), Point(2, 3), Point(4, 2)]
}

gdf_points = gpd.GeoDataFrame(points_data, crs='EPSG:4326')

polygons_data = {    #B
    'District': ['District 1', 'District 2'],
    'geometry': [Polygon([(0, 0), (0, 4), (4, 4), (4, 0)]), Polygon([(3, 1), (3, 5), (6, 5), (6, 1)])]
}

gdf_polygons = gpd.GeoDataFrame(polygons_data, crs='EPSG:4326')

gdf_points.to_csv('points_before_join.csv', index=False)    #C
gdf_polygons.to_csv('polygons_before_join.csv', index=False)

additional_points_data = {    #D
    'City': ['City D', 'City E', 'City F'],
    'Population': [300000, 200000, 400000],
    'geometry': [Point(6, 6), Point(5, 2), Point(7, 3)]
}

gdf_additional_points = gpd.GeoDataFrame(additional_points_data, crs='EPSG:4326')

gdf_points_all = gpd.GeoDataFrame(pd.concat([gdf_points, gdf_additional_points], ignore_index=True), crs='EPSG:4326')    #E

joined_gdf = gpd.sjoin(gdf_points_all, gdf_polygons, how='inner', op='within')    #F

joined_gdf.to_csv('joined_data.csv', index=False)    #G

fig, ax = plt.subplots(figsize=(8, 6))
gdf_polygons.plot(ax=ax, color='lightgray', edgecolor='black', alpha=0.7, label='Polygons')

gdf_points_all.plot(ax=ax, color='blue', markersize=100, label='Cities (Outside Polygons)')

joined_gdf.plot(ax=ax, color='red', markersize=100, label='Points within Polygons')

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Spatial Join: Points within Polygons')

ax.legend()

plt.show()
#A Create a GeoDataFrame for points data
#B Create a GeoDataFrame for polygons data
#C Save the data before spatial join to CSV files
#D Create additional points outside the polygons
#E Combine the original points and additional points
#F Perform spatial join (points within polygons)
#G Save the data after spatial join to a CSV file
