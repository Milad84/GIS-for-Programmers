import numpy as np
import matplotlib.pyplot as plt

historical_x = np.array([10, 20, 30, 40, 50])    #A
historical_y = np.array([20, 40, 50, 60, 70])

georeferenced_x = np.array([12, 22, 33, 42, 52])    #B
georeferenced_y = np.array([21, 43, 52, 63, 73])

displacement_x = georeferenced_x - historical_x    #C
displacement_y = georeferenced_y - historical_y

plt.figure(figsize=(8, 6))
plt.scatter(historical_x, historical_y, label='Historical Maps', color='blue')
plt.scatter(georeferenced_x, georeferenced_y, label='Georeferenced Maps', color='red')
for i in range(len(historical_x)):
    plt.arrow(historical_x[i], historical_y[i], displacement_x[i], displacement_y[i],
              head_width=1, head_length=1, fc='gray', ec='gray', alpha=0.7)
plt.xlabel('X Coordinates')
plt.ylabel('Y Coordinates')
plt.title('Georeferencing Historical Maps')
plt.legend()
plt.grid(True)
plt.show()
#A Synthetic data for historical maps (original coordinates)
#B Synthetic data for georeferenced historical maps (transformed coordinates)
#C Calculate displacement vectors
