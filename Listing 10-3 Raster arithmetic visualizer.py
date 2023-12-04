import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Function to get the value of a specific pixel in a raster dataset
def get_pixel_value(raster, row, col):
    return raster.read(1, window=((row, row + 1), (col, col + 1)))[0, 0]

# Function to get the middle pixel of a raster dataset
def get_middle_pixel(raster):
    height, width = raster.shape
    return height // 2, width // 2

# Function to perform the arithmetic operation on two raster datasets
def perform_arithmetic_operation(raster_path1, raster_path2):
    # Read raster datasets using rasterio
    with rasterio.open(raster_path1) as raster1, rasterio.open(raster_path2) as raster2:
        # Get the middle pixel of each raster
        row, col = get_middle_pixel(raster1.read(1))
        value_raster1 = get_pixel_value(raster1, row, col)

        row, col = get_middle_pixel(raster2.read(1))
        value_raster2 = get_pixel_value(raster2, row, col)

        # Perform arithmetic operations on raster datasets (e.g., addition)
        band1 = raster1.read(1).astype(np.float32)  # Cast to a common data type (float32)
        band2 = raster2.read(1).astype(np.float32)  # Cast to a common data type (float32)
        result_array = band1 + band2
        value_result_raster = result_array[row, col]

        # Display the pixel values of the specified pixel in each raster
        print("Pixel Values of the Specified Pixel:")
        print(f"Raster 1: {value_raster1}")
        print(f"Raster 2: {value_raster2}")
        print(f"Resulting Raster: {value_result_raster}")

        # Create subplots to show individual raster datasets
        plt.figure(figsize=(15, 5))

        # Subplot for raster1
        plt.subplot(1, 3, 1)
        plt.imshow(band1, cmap='viridis', aspect='auto')
        plt.title('Raster 1 (Band 1)')
        plt.xlabel('Column #')
        plt.ylabel('Row #')
        plt.text(col, row, value_raster1, color='red', fontsize=12, ha='center', va='center')

        # Subplot for raster2
        plt.subplot(1, 3, 2)
        plt.imshow(band2, cmap='viridis', aspect='auto')
        plt.title('Raster 2 (Band 2)')
        plt.xlabel('Column #')
        plt.ylabel('Row #')
        plt.text(col, row, value_raster2, color='red', fontsize=12, ha='center', va='center')

        # Subplot for the combined result
        plt.subplot(1, 3, 3)
        plt.imshow(result_array, cmap='viridis', aspect='auto')
        plt.title('Arithmetic Operation Result')
        plt.xlabel('Column #')
        plt.ylabel('Row #')
        plt.text(col, row, value_result_raster, color='red', fontsize=12, ha='center', va='center')

        # Adjust the layout for better visualization
        plt.tight_layout()
        plt.show()

# Example file paths for two raster datasets on your computer (replace with actual paths)
raster_path1 = 'D:\LC08_L1TP_023031_20230511_20230518_02_T1\LC08_L1TP_023031_20230511_20230518_02_T1_B1.tif'
raster_path2 = 'D:\LC08_L1TP_023031_20230511_20230518_02_T1\LC08_L1TP_023031_20230511_20230518_02_T1_B11.tif'

# Perform arithmetic operation on the provided raster datasets
perform_arithmetic_operation(raster_path1, raster_path2)
