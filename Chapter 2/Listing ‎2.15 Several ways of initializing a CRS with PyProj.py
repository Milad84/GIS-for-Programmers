from pyproj import CRS

crs = CRS.from_epsg(4326)
crs = CRS.from_string("EPSG:4326")
crs = CRS.from_proj4("+proj=latlon")
crs = CRS.from_user_input(4326)
