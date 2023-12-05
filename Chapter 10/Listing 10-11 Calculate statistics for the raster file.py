import rasterio

raster_path = 'path/to/your/raster/file.tif'

with rasterio.open(raster_path) as src:
    data = src.read(1)  # Assuming the raster has a single band

    mean = data.mean()
    minimum = data.min()
    maximum = data.max()
    std_dev = data.std()

print("Raster Statistics:")
print("Mean:", mean)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard Deviation:", std_dev)
