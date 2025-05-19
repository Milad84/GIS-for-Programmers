import numpy as np
import matplotlib.pyplot as plt

city_size = 100    #A
traffic_data = np.random.rand(city_size, city_size) * 100  # Random traffic values (0 to 100)

road_network = np.zeros((city_size, city_size))    #B
road_network[30:70, 20:80] = 1  

combined_data = traffic_data * road_network    #C

plt.figure(figsize=(10, 10))    #D
plt.imshow(combined_data, cmap='hot', interpolation='nearest')
plt.title('Traffic Heatmap')
plt.colorbar(label='Traffic Density')
plt.show()
#A Generate synthetic traffic data for a grid representing a city
#B Generate synthetic road network raster
#C Combine traffic data with road network
#D Create a traffic heatmap
