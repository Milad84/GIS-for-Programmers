import geopandas as gpd
from shapely.geometry import LineString
import matplotlib.pyplot as plt

river1_data = {    #A
    'Name': ['River 1'],
    'geometry': [LineString([(0, 0), (2, 4), (4, 2)])]
}

river2_data = {    #B
    'Name': ['River 2'],
    'geometry': [LineString([(4, 2), (6, 4), (8, 0)])]
}

river1_gdf = gpd.GeoDataFrame(river1_data, crs='EPSG:4326')    #C
river2_gdf = gpd.GeoDataFrame(river2_data, crs='EPSG:4326')

appended_river_gdf = river1_gdf.append(river2_gdf)    #D

fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharex=True, sharey=True)

river1_gdf.plot(ax=axs[0], color='blue', linewidth=2, label='River 1')
axs[0].set_title('River 1')

river2_gdf.plot(ax=axs[1], color='green', linewidth=2, label='River 2')
axs[1].set_title('River 2')

appended_river_gdf.plot(ax=axs[2], color='red', linewidth=2, label='Appended River')    #E
axs[2].set_title('Appended River')

fig.suptitle('Rivers', fontsize=16)
for ax in axs:
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.legend()

plt.show()
#A Create the first set of lines representing the river
#B Create the second set of lines representing the river
#C Create Geopandas GeoDataFrames from the data
#D Append river2_gdf to river1_gdf 
#E Plot the appended river (in red) 
