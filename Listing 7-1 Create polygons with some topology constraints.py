from shapely.geometry import Point, Polygon
from shapely.ops import cascaded_union
import matplotlib.pyplot as plt

def create_polygons(points):
    polygons = [Point(point).buffer(1) for point in points]    #A
    merged_polygon = cascaded_union(polygons)    #B

    if merged_polygon.geom_type == 'MultiPolygon':    #C
        polygons = list(merged_polygon)
    else:
        polygons = [merged_polygon]

    return polygons

points = [(3, 3), (4, 4), (5, 5), (6, 6)]  
polygons = create_polygons(points)
fig, ax = plt.subplots()
for polygon in polygons:
    x, y = polygon.exterior.xy
    ax.plot(x, y)
ax.set_aspect('equal', 'box')
plt.show()
#A Create individual polygons from the points
#B Apply topological rules
#C Convert multi-polygon to individual polygons
