import geopandas as gpd
import pandas as pd

data1 = {    #A
    'City': ['City A', 'City B'],
    'Population': [1000000, 500000],
    'Area': [150, 300]
}

data2 = {
    'City': ['City C', 'City D'],
    'Population': [800000, 200000],
    'Area': [200, 250]
}

gdf1 = gpd.GeoDataFrame(data1, geometry=gpd.points_from_xy([1, 2], [3, 4]), crs='EPSG:4326')
gdf2 = gpd.GeoDataFrame(data2, geometry=gpd.points_from_xy([3, 4], [2, 1]), crs='EPSG:4326')

merged_gdf = gpd.GeoDataFrame(pd.concat([gdf1, gdf2], ignore_index=True), crs='EPSG:4326')    #B

print(merged_gdf)
#A Create two GeoDataFrames with the same data structure
#B Merge the two GeoDataFrames
