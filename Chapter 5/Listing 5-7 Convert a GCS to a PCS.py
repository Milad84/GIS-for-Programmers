import geopandas as gpd
import matplotlib.pyplot as plt

wrld = gpd.read_file("https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_land.geojson")

def map_data(data, header):

    fig, ax = plt.subplots(figsize = (10, 5))
    colors = ["#762A19"]
    for i in range(0, len(data)):
        data[i].plot(facecolor = colors[i], ax = ax)

    plt.title(header)
    plt.style.use("bmh")
    plt.tight_layout()

map_data([wrld], "Map of the World")
plt.show()
print("CRS: {}".format(wrld.crs))
wrld_reproject_proj4 = wrld.copy()


mercator = wrld_reproject_proj4.to_crs("EPSG:3395")    #A
map_data([mercator ], "Map of the World")
plt.show()
print(mercator.crs)    #B
#A Conversion from 4326 (GCS) to 3395 (PCS)
#B Verify the conversion
