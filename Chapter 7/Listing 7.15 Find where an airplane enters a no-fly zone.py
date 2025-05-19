import geopandas as gpd
from shapely.geometry import LineString, Polygon
import folium
import webbrowser

airplane_path_data = {    #A
    'Flight_Number': ['Flight 123'],
    'geometry': [LineString([(-90, 40), (-85, 35), (-80, 30), (-75, 35), (-70, 40), (-65, 45)])]
}
airplane_path_gdf = gpd.GeoDataFrame(airplane_path_data, crs='EPSG:4326')

no_fly_zone_data = {    #B
    'Zone_Name': ['Restricted Zone'],
    'geometry': [Polygon([(-85, 32), (-75, 32), (-75, 38), (-85, 38), (-85, 32)])]
}
no_fly_zone_gdf = gpd.GeoDataFrame(no_fly_zone_data, crs='EPSG:4326')

airplane_path_gdf = airplane_path_gdf.to_crs(epsg=3395)    #C
no_fly_zone_gdf = no_fly_zone_gdf.to_crs(epsg=3395)

intersects_no_fly_zone_gdf = gpd.overlay(airplane_path_gdf, no_fly_zone_gdf, how='intersection')    #D

m = folium.Map(location=[38, -80], zoom_start=6, tiles='OpenStreetMap')    #E

folium.GeoJson(airplane_path_gdf, name='Airplane Path').add_to(m)    #F

folium.GeoJson(no_fly_zone_gdf, name='No-Fly Zone', style_function=lambda feature: {'color': 'red'}).add_to(m)    #G

if not intersects_no_fly_zone_gdf.empty:    #H

    folium.GeoJson(intersects_no_fly_zone_gdf, name='Intersection with No-Fly Zone', style_function=lambda feature: {'color': 'orange'}).add_to(m)

folium.LayerControl().add_to(m)    #I

map_file = 'airplane_path_no_fly_zone_map.html'
m.save(map_file)
webbrowser.open(map_file)    #J
#A Create a GeoDataFrame for the airplane path
#B Create a GeoDataFrame for the no-fly zone
#C Reproject GeoDataFrames to a projected CRS (e.g., EPSG:3395, World Mercator)
#D Perform the intersection operation to find if the airplane path intersects with the no-fly zone
#E Create a folium map to visualize airplane path and a no-fly zone
#F Add airplane path to the map
#G Add a no-fly zone to the map
#H Check if there is an intersection
#I Add Layer Control to toggle map layers
#J Save the map as an HTML file and open it automatically in the default web browser
