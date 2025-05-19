import rasterio
import numpy as np
import matplotlib.pyplot as plt
from pyproj import CRS, Transformer
from rasterio.warp import calculate_default_transform, reproject, Resampling

def find_highest_elevation(raster_file, target_crs=None):
    with rasterio.open(raster_file) as dataset:
        if target_crs is not None:    #A
            dst_crs = CRS.from_string(target_crs)
        else:
            dst_crs = dataset.crs

        transform, width, height = calculate_default_transform (dataset.crs, dst_crs, dataset.width,
        dataset.height, *dataset.bounds)    #B
        raster_data = np.empty((height, width), dtype=np.float32)    #C
        reproject(    #D
            source=dataset.read(1),
            destination=raster_data,
            src_transform=dataset.transform,
            src_crs=dataset.crs,
            dst_transform=transform,
            dst_crs=dst_crs,
            resampling=Resampling.nearest
        )

        highest_elevation = np.max(raster_data)    #E
        highest_indices = np.where(raster_data == highest_elevation)    #F

        highest_coordinates = []    #G
        for row, col in zip(highest_indices[0], highest_indices[1]):
            x, y = rasterio.transform.xy(transform, row, col)
            highest_coordinates.append((x, y))

        plt.figure(figsize=(8, 6))
        plt.imshow(raster_data, cmap='terrain',
        extent=(transform[2],
        transform[2] + width * transform[0],
        transform[5] +  height * transform[4],transform[5]),origin='upper')

        plt.colorbar(label='Elevation (meters)')
        plt.scatter([coord[0] for coord in highest_coordinates],
        [coord[1]
for coord in highest_coordinates],
        color='red',   marker='x', s=100, label='Highest Elevation')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Elevation Map with Highest Elevation')
        plt.legend()
        plt.show()

        return highest_elevation, highest_coordinates

if __name__ == '__main__':
    raster_file = 'D:/LC09_L1TP_023031_20230503_20230503_02_T1_refl - Copy.tif'
    target_crs = 'EPSG:4326'
    highest_elevation, highest_coordinates = find_highest_elevation(raster_file, target_crs=target_crs)
    print("Highest Elevation:", highest_elevation, "meters")
    print("Coordinates of Highest Elevation Cell(s):", highest_coordinates)
#A Project the raster data to the target CRS
#B Calculate the transformation parameters for the target CRS
#C Create an empty array to store the reprojected raster data
#D Reproject the raster data
#E Get the elevation value of the highest cell
#F Get the indices of the highest cell(s) in the raster data
#G Calculate the coordinates of the highest cell(s)
