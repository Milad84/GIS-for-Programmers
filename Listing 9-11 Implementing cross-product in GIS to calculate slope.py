from osgeo import gdal
import numpy as np
from tqdm import tqdm

dem_path = "PATH TO A DEM ON YOUR SYSTEM.tif"    #A
dataset = gdal.Open(dem_path)
band = dataset.GetRasterBand(1)
dem_array = band.ReadAsArray()

cell_size = 1.0    #B  

slope_array = np.zeros_like(dem_array, dtype=np.float32)    #C

total_cells = (dem_array.shape[0] - 2) * (dem_array.shape[1] - 2)    #D


pbar = tqdm(total=total_cells, desc="Calculating slope", unit="cells")
    #E
for row in range(1, dem_array.shape[0] - 1):    #F
    for col in range(1, dem_array.shape[1] - 1):
        z_center = dem_array[row, col]    #G
        z_left = dem_array[row, col - 1]
        z_right = dem_array[row, col + 1]
        z_up = dem_array[row - 1, col]
        z_down = dem_array[row + 1, col]

        AB = np.array([cell_size, 0, z_right - z_left])    #H
        AC = np.array([0, cell_size, z_down - z_up])
        
        normal_vector = np.cross(AB, AC)    #I

        
        slope = np.arctan(np.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2) / normal_vector[2])    #J

        slope_array[row, col] = slope    #K

        pbar.update(1)    #L

pbar.close()    #M

output_path = "D:/slope.tif"    #N
driver = gdal.GetDriverByName("GTiff")
output_dataset = driver.Create(output_path, dem_array.shape[1], dem_array.shape[0], 1, gdal.GDT_Float32)
output_dataset.GetRasterBand(1).WriteArray(slope_array)
output_dataset.SetGeoTransform(dataset.GetGeoTransform())
output_dataset.SetProjection(dataset.GetProjection())
output_dataset.FlushCache()
output_dataset = None

dataset = None    #O
#A Read the DEM raster file
#B Define the cell size (assuming square cells) or use the actual cell size from the DEM metadata
#C Calculate the slope for each cell
#D Get the total number of cells
#E Initialize the progress bar
#F Iterate over each cell in the DEM 
#G Get the elevation values of the cell and its neighboring cells
#H Calculate the vectors AB and AC using neighboring elevations
#I Calculate the cross product
#J Calculate the slope using the magnitude of the normal vector
#K Assign the slope value to the corresponding cell in the slope array
#L Update the progress bar 
#M Close the progress bar
#N Save the slope array as a new raster
#O Close the input dataset
