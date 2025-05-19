import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))    #A

fig, axs = plt.subplots(1, 2, figsize=(15, 7))

world.to_crs(epsg=4326).plot(ax=axs[0], edgecolor='k', color='lightgray')
axs[0].set_title('WGS 1984 (EPSG:4326)')    #B
axs[0].set_xlabel('Longitude (degrees)')
axs[0].set_ylabel('Latitude (degrees)')

world.to_crs(epsg=3857).plot(ax=axs[1], edgecolor='k', color='lightgray')
axs[1].set_title('Web Mercator (EPSG:3857)')    #C
axs[1].set_xlabel('Web Mercator X (meters)')
axs[1].set_ylabel('Web Mercator Y (meters)')

axs[1].set_xlim([-20026376.39, 20026376.39])    #D
axs[1].set_ylim([-20048966.10, 20048966.10])

plt.tight_layout()

plt.show()

#A Load natural earth data for countries
#B Left subplot: WGS 1984 (EPSG:4326)
#C Right subplot: Web Mercator (EPSG:3857)
#D Set the extent for the right subplot to avoid the south pole extension. It is recommended to run the code without setting an extent to see the real result of the projection.
