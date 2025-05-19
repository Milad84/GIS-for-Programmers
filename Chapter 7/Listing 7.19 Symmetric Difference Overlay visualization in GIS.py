from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from matplotlib.patches import polygon as mpl_polygon

def plot_polygon(polygon, ax, color):
    mpl_poly = mpl_polygon(list(polygon.exterior.coords), facecolor=color, alpha=0.7)
    ax.add_patch(mpl_poly)

def symmetric_difference(layer1, layer2):
    
    polygon1 = Polygon(layer1)    #A
    polygon2 = Polygon(layer2)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    plot_polygon(polygon1, ax, 'red')    #B

    plot_polygon(polygon2, ax, 'blue')    #C

    result = polygon1.symmetric_difference(polygon2)    #D

    if result.geom_type == 'Polygon':    #E
        plot_polygon(result, ax, 'green')
    elif result.geom_type == 'MultiPolygon':
        for poly in result:
            plot_polygon(poly, ax, 'green')

    shared_portion = polygon1.intersection(polygon2)    #F
    if shared_portion.geom_type == 'Polygon':
        plot_polygon(shared_portion, ax, 'yellow')
    elif shared_portion.geom_type == 'MultiPolygon':
        for poly in shared_portion:
            plot_polygon(poly, ax, 'yellow')

    plt.xlim(min(layer1 + layer2)[0] - 1, max(layer1 + layer2)[0] + 1)
    plt.ylim(min(layer1 + layer2)[1] - 1, max(layer1 + layer2)[1] + 1)
    plt.show()


layer1 = [(0, 0), (0, 2), (2, 2), (2, 0)]
layer2 = [(1, 1), (1, 3), (3, 3), (3, 1)]

fig, ax = plt.subplots()
ax.set_aspect('equal')
plot_polygon(Polygon(layer1), ax, 'red')
plt.xlim(min(layer1)[0] - 1, max(layer1)[0] + 1)
plt.ylim(min(layer1)[1] - 1, max(layer1)[1] + 1)
plt.show()

fig, ax = plt.subplots()
ax.set_aspect('equal')
plot_polygon(Polygon(layer2), ax, 'blue')
plt.xlim(min(layer2)[0] - 1, max(layer2)[0] + 1)
plt.ylim(min(layer2)[1] - 1, max(layer2)[1] + 1)
plt.show()

symmetric_difference(layer1, layer2)    #G
#A Create Shapely polygons from input layers
#B Plot layer1 in red
#C Plot layer2 in blue
#D Compute symmetric difference
#E Plot symmetric difference in green
#F Plot shared portion in yellow
#G Compute and visualize the symmetric difference
