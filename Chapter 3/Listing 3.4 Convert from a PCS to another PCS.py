import pyproj

source_pcs = pyproj.CRS("EPSG:3857")    #A
target_pcs = pyproj.CRS("EPSG:32633")    #B

transformer = pyproj.Transformer.from_crs(source_pcs, target_pcs, always_xy=True)    #C

points_source = [(x1, y1), (x2, y2), (x3, y3)]    #D
points_target = [transformer.transform(x, y) for x, y in points_source]    #E

for point in points_target:
    print("Transformed coordinates:", point)
  
#A Define the source coordinate system (e.g., Web Mercator) 
#B Define the target coordinate system (e.g., WGS 84 / UTM Zone 33N)
#C Create a transformer object for coordinate transformation
#D Define a list of points in the source PCS
#E Transform the points from the source PCS to the target PCS 

