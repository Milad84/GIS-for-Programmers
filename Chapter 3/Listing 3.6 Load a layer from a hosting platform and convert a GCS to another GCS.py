import geopandas as gpd    #A
import matplotlib.pyplot as plt    #A

wrld = gpd.read_file("https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_land.geojson")    #B

def map_data(data, header):    #C

    fig, ax = plt.subplots(figsize = (10, 5))
    colors = ["#762A19"]
    for i in range(0, len(data)):
        data[i].plot(facecolor = colors[i], ax = ax)

    plt.title(header)
    plt.style.use("bmh")
    plt.tight_layout()

map_data([wrld], "Map of the World")    #D
plt.show()
print("CRS: {}".format(wrld.crs))    #E
wrld_reproject_proj4 = wrld.copy()    #F

wrld_reproject_proj4 = wrld_reproject_proj4.to_crs("+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs +type=crs")    #G

map_data([wrld_reproject_proj4 ], "Map of the World")    #H
plt.show()
print(wrld_reproject_proj4.crs)    #I

#A Import needed libraries
#B Call the hosted layer
#C Create the function to set parameters for the visualization
#D Create an instance of the object
#E Get CRS for the geojson layer
#F Create a copy of data and start converting to another GCS
#G Transform to epsg 4269. Notice the seven paramters for +towgs84
#H Create another instance of the object with the new parameters for GCS
#I Verify the parameters of the new GCS

