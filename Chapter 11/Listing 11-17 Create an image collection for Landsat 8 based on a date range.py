roi = ee.Geometry.Rectangle([-122.60, 37.45, -122.35, 37.65])    #A

collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA') \    #B
    .filterBounds(roi) \
    .filterDate('2020-01-01', '2020-12-31')
#A Define a region of interest (ROI)
#B Create an image collection for Landsat 8
