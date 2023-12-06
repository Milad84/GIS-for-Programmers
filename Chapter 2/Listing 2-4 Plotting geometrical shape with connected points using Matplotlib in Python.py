import matplotlib.pyplot as plt

points = [    #A
    (2, 3),
    (5, 8),
    (7, 5),
    (4, 1),
    (2, 3)  
]

x_coords, y_coords = zip(*points)    #B

plt.scatter(x_coords, y_coords)    #C

plt.plot(x_coords, y_coords)    #D

plt.title("Geometrical Shape")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.show()
#A Imaginary points with known coordinates (surveyed points)
#B Extract x and y coordinates from points
#C Visualize
#D Connect points with lines
