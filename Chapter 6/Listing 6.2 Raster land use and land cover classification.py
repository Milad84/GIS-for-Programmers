import rasterio
from rasterio.plot import show
from rasterio.enums import Resampling
import numpy as np

dataset = rasterio.open('sample_raster.tif')    #A

raster_data = dataset.read(1)    #B

show(raster_data)

land_use_categories = {    #C
    1: 'Urban',
    2: 'Agricultural',
    3: 'Forest',
    4: 'Water',
    5: 'Barren',
    6: 'Other'
}

classified_data = np.zeros_like(raster_data, dtype=np.uint8)    #D
for category_code, category_name in land_use_categories.items():
    classified_data[raster_data == category_code] = category_code

show(classified_data, cmap='Set1', title='Land Use and Land Cover')

unique, counts = np.unique(classified_data, return_counts=True)    #E
for category_code, count in zip(unique, counts):
    if category_code in land_use_categories:
        category_name = land_use_categories[category_code]
        print(f"{category_name}: {count} pixels")
#A Open the raster dataset
#B Assuming a single-band raster, change the index if there are multiple bands
#C Define land use and land cover categories
#D Perform land use and land cover classification
#E Print the statistics of land use and land cover

