import geopandas as gpd

layer1 = gpd.read_file('path_to_layer1.shp')    #A  
layer2 = gpd.read_file('path_to_layer2.shp')    

overlay_result = gpd.overlay(layer1, layer2, how='intersection')    #B

print(overlay_result.head())
#A Read the input data layers
#B Perform the overlay operation
