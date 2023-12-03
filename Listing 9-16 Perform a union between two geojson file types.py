import geopandas as gpd
import matplotlib.pyplot as plt

file1 = 'path_to_file1.geojson'    #A 
file2 = 'path_to_file2.geojson'  

gdf1 = gpd.read_file(file1)    #B
gdf2 = gpd.read_file(file2)

union_result = gpd.overlay(gdf1, gdf2, how='union')    #C

fig, ax = plt.subplots(figsize=(10, 10))
union_result.plot(ax=ax, color='red', edgecolor='black')
gdf1.plot(ax=ax, color='blue', edgecolor='black', alpha=0.5)
gdf2.plot(ax=ax, color='green', edgecolor='black', alpha=0.5)

ax.set_title('Union Result')
plt.show()
#A Read the input GeoJSON files
#B Read the GeoJSON data into GeoDataFrames
#C Perform the union operation

