import laspy
import open3d as o3d
import numpy as np

las = laspy.read("D:/USGS_LPC_AZ_MaricopaPinal_2020_B20_w0361n3688.las")

print (las.header)
print (las.header.point_format)    #A
print (las.header.point_count)    #B
print (las.vlrs)    #C
print (list(las.point_format.dimension_names))    #D
print (las.X)    #E
print (las.intensity)    #F
print (las.gps_time)    #G
print (set(list(las.classification)))    #H
point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))    #I
geom = o3d.geometry.PointCloud()    #J
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
#A returns the format of the points in the LAS file (stored as XYZ coordinates, RGB values, etc.)
#B returns the total number of points in the LAS file
#C returns any Variable Length Record (VLR) information in the LAS file
#D returns a list of dimension names (e.g., X, Y, Z, Intensity) in the LAS file
#E returns the X coordinates of the points
#F returns the intensity values associated with the points
#G returns the GPS time associated with the points
#H returns a set of classification values present in the LAS file, representing different classes or categories of the points
#I create a NumPy array point_data by stacking the X, Y, and Z coordinate arrays from the LAS file using np.stack(). The axis=0 argument specifies that the stacking should be done along the first axis (creating a 3 x n array). The subsequent transpose((1, 0)) operation swaps the dimensions to make it an n x 3 array
#J creates an Open3D PointCloud object named geom and assigns the point_data array to its points attribute. This prepares the point cloud data for visualization using Open3D.
