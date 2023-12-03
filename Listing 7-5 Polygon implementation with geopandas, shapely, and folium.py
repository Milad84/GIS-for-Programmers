import geopandas as gpd
from shapely.geometry import Polygon
import folium

lat_points = [34.564367,43.458899,20.643578,10.445568,14.567932]    #A
lon_points = [23.472233,17.905633,23.4804411,10.906675,23.3267788]    #B

polygon_geom = Polygon(zip(lon_points, lat_points))    #C
polygon = gpd.GeoDataFrame(crs='epsg:4326', geometry=[polygon_geom])    #D


map = folium.Map([34.563422, 12.467798], zoom_start=3,    #E tiles='openstreetmap')    #F
folium.GeoJson(polygon).add_to(map)    #G
folium.LatLngPopup().add_to(map)    #H

map.save(r"D:\index.html")    #I
#A List of latitudes
#B List of longitudes
#C Using the zip function to combine lats and longs
#D Define CRS and geometry
#E Set the center point of the map and zoom level
#F Here, the code uses “openstreetmap” as the tile system
#G Add the polygon to the map
#H Use LatLngPopup() to get the lat and long upon clicking anywhere on the map
#I Save the result as an HTML file and open it in a browser
