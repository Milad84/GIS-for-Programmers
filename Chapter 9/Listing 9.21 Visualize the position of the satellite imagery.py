import folium

map = folium.Map(location=[37.55, -122.475], zoom_start=10)    #A

roi_geojson = ee.FeatureCollection(roi).getInfo()    #B
folium.GeoJson(roi_geojson).add_to(map)

map.save('map.html')    #C
#A Create a map centered around the ROI
#B Add the ROI boundary as a GeoJSON layer
#C The output will be saved as an HTML file in the content folder
