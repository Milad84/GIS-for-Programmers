import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def convert_coordinates(point, source_crs, target_crs):
    
    conversion_factor = 111000    #A
    converted_point = [coord * conversion_factor for coord in point]

    return converted_point

source_point = (10, 20, 100)    #B

source_crs = "EPSG:4326"      #C 
target_crs = "EPSG:32633"    #D  

target_point = convert_coordinates(source_point, source_crs, target_crs)    #E

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(*source_point, c='red', marker='o', label='Source Point (degrees)')
ax1.set_title('Source Coordinate System (degrees)')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.set_zlabel('Elevation')

ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(*target_point, c='blue', marker='o', label='Target Point (meters)')
ax2.set_title('Target Coordinate System (meters)')
ax2.set_xlabel('X (meters)')
ax2.set_ylabel('Y (meters)')
ax2.set_zlabel('Z (meters)')

ax1.legend()
ax2.legend()

plt.tight_layout()

plt.show()
