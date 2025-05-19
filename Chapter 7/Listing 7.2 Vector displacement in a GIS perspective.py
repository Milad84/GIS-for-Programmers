from pyproj import Transformer

point1 = (40.7128, -74.0060)    #A
point2 = (51.5074, -0.1278)   

transformer = Transformer.from_crs("EPSG:4326", "EPSG:27700", always_xy=True)    #B

point1_transformed = transformer.transform(*point1)    #C
point2_transformed = transformer.transform(*point2)

displacement = (point2_transformed[0] - point1_transformed[0], point2_transformed[1] - point1_transformed[1])    #D

print("Displacement vector:", displacement)
#A Define the coordinates of two points in WGS84
#B Create a transformer for coordinate transformation
#C Transform the points to a different coordinate system (e.g., British National Grid - EPSG:27700)
#D Calculate the displacement vector
