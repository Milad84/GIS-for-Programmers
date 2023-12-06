from shapely.geometry import LineString
from shapely.ops import polygonize
import matplotlib.pyplot as plt

def create_buffer_from_line(line, buffer_distance):
    buffer_polygon = line.buffer(buffer_distance)
    polygons = list(polygonize(buffer_polygon))
    return polygons
line = LineString([(1, 1), (3, 4), (6, 2), (9, 7)])  
buffer_distance = 1.5  
polygons = create_buffer_from_line(line, buffer_distance)
fig, ax = plt.subplots()
for polygon in polygons:
    x, y = polygon.exterior.xy
    ax.plot(x, y)
ax.set_aspect('equal', 'box')
plt.show()
