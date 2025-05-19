import geopandas as gpd
from shapely.geometry import Point

data = {'City': ['New York', 'Los Angeles', 'Chicago'],    #A
        'Latitude': [40.7128, 34.0522, 41.8781],
        'Longitude': [-74.0060, -118.2437, -87.6298]}

geometry = [Point(xy) for xy in zip(data['Longitude'], data['Latitude'])]

geo_df = gpd.GeoDataFrame(data, geometry=geometry)

geo_df.sindex    #B

bbox = (-120, 30, -80, 45)    #C
possible_matches_index = list(geo_df.sindex.intersection(bbox))
possible_matches = geo_df.iloc[possible_matches_index]

print("Original Dataset:")
print(geo_df)
print("\nData within the Bounding Box:")
print(possible_matches)
#A Create a geospatial dataset
#B Create a spatial index
#C Query the dataset using the spatial index. Example: bounding box

