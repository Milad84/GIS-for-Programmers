
import pyproj

source_crs = pyproj.CRS.from_string('EPSG:4326')    #A  
target_crs = pyproj.CRS.from_string('EPSG:3857')    #B    

transformer = pyproj.Transformer.from_crs(source_crs, target_crs, always_xy=True)    #C

source_latitude = 40.7128  #D 
source_longitude = -74.0060  #E

target_x, target_y = transformer.transform(source_longitude, source_latitude)    #F

print("Transformed Coordinates (x, y):", target_x, target_y)
#A Define the source coordinate system 
#B Define the target coordinate system (A projected coordinate system)
#C Create a transformer object for coordinate transformation
#D New York City latitude in decimal degrees
#E New York City longitude in decimal degrees
#F Perform the coordinate transformation
