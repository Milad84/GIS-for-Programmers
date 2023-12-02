import pyproj

itrf_x = 1234567.89    #A
itrf_y = 9876543.21
itrf_z = 5432109.87


transformer = pyproj.Transformer.from_crs("EPSG:7789", "EPSG:4326",    #B always_xy=True)

lon, lat, _ = transformer.transform(itrf_x, itrf_y, itrf_z)    #C

print("Latitude:", lat)
print("Longitude:", lon)
#A Define the ITRF geometric coordinate in meters
#B Create a pyproj transformer for the conversion from an ITRF system to a geodetic system
#C Convert ITRF coordinates to latitude and longitude 

