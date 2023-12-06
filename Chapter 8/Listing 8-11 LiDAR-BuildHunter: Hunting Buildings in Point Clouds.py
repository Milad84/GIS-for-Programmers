import laspy
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


las = laspy.read("path_to_lidar_data.las")

features = np.array(...)  
labels = np.array(...)  

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
building_points = las.points[labels == 1]  buildings
ax.scatter(building_points['X'], building_points['Y'], building_points['Z'], c='red', marker='.', label='Buildings')
non_building_points = las.points[labels == 0]  
ax.scatter(non_building_points['X'], non_building_points['Y'], non_building_points['Z'], c='blue', marker='.', label='Non-Buildings')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
