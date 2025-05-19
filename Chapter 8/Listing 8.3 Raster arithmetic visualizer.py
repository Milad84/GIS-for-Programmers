import rasterio
import numpy as np
import matplotlib.pyplot as plt

def get_pixel_value(raster, row, col):    #A
    return raster.read(1, window=((row, row + 1), (col, col + 1)))[0, 0]

def get_middle_pixel(raster):    #B
    height, width = raster.shape
    return height // 2, width // 2

def perform_arithmetic_operation(raster_path1, raster_path2):    #C
    with rasterio.open(raster_path1) as raster1, rasterio.open(raster_path2) as raster2:
        row, col = get_middle_pixel(raster1.read(1))
        value_raster1 = get_pixel_value(raster1, row, col)

        row, col = get_middle_pixel(raster2.read(1))
        value_raster2 = get_pixel_value(raster2, row, col)

        band1 = raster1.read(1).astype(np.float32)    #D
        band2 = raster2.read(1).astype(np.float32)  
        result_array = band1 + band2
        value_result_raster = result_array[row, col]

raster_path1 = 'D:\LC08_L1TP_023031_20230511_20230518_02_T1\LC08_L1TP_023031_20230511_20230518_02_T1_B1.tif'
raster_path2 = 'D:\LC08_L1TP_023031_20230511_20230518_02_T1\LC08_L1TP_023031_20230511_20230518_02_T1_B11.tif'

perform_arithmetic_operation(raster_path1, raster_path2)
#A Function to get the value of a specific pixel in a raster dataset
#B Function to get the middle pixel of a raster dataset
#C Function to perform the arithmetic operation on two raster datasets
#D Perform arithmetic operations on raster datasets and cast to a common data type (float32)

