from pyproj import Transformer

transformer = Transformer.from_crs(4326, 3857)
x1, y1 = transformer.transform(-33, 98)

print(x1, y1)
