import geopandas as gpd
import matplotlib.pyplot as plt

rivers_path = "D:/Rivers_Azerbaijan/riverl_aze.shp"
rivers_data = gpd.read_file(rivers_path)

rivers_data['length'] = rivers_data.geometry.length
river_lengths = rivers_data['length'].tolist()

plt.hist(river_lengths, bins=20)
plt.xlabel("River Length")
plt.ylabel("Frequency")
plt.title("Distribution of River Lengths")
plt.show()
