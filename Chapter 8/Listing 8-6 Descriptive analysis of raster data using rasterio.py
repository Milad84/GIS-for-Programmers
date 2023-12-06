import rasterio

path =  "D:\LC09_L1TP_023031_20230503_20230503_02_T1_refl.tif"

img = rasterio.open(path)    #B
#show(img)

bands = img.count
image_width= img.width
image_height= img.height

print (bands)
print (image_width)
print(image_height)
