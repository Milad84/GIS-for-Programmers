from pyproj.crs import GeographicCRS
geog_crs = GeographicCRS()
geog_proj = geog_crs.to_proj4()
print(geog_proj)
