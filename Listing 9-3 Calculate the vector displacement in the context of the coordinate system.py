from pyproj import Transformer
import matplotlib.pyplot as plt

point1 = (40.7128, -74.0060)  
point2 = (51.5074, -0.1278)   

transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)

point1_transformed = transformer.transform(*point1)
point2_transformed = transformer.transform(*point2)


plt.scatter(point1_transformed[0], point1_transformed[1], color='red', label='New York')
plt.scatter(point2_transformed[0], point2_transformed[1], color='blue', label='London')


plt.title("Point Positions on Map")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.legend()

plt.show()
