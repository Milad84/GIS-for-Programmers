from pyproj import Transformer    #A
transformer = Transformer.from_crs(4326, 2100)
points = [(22.95, 40.63), (22.81, 40.53), (23.51, 40.86)]
for pt in transformer.itransform(points):
    print (pt)
#A Transformer is the main class in PyProj to convert coordinate systems
