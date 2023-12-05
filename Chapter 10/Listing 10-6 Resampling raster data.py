from osgeo import gdal

input_path = "D:\LC08_L1TP_023031_20230511_20230518_02_T1\LC08_L1TP_023031_20230511_20230518_02_T1_B1.tif"    #A
output_path = "D:\output_resampled.tif"    

input_dataset = gdal.Open(input_path)    #B

input_geotransform = input_dataset.GetGeoTransform()    #C

new_resolution = 60.0    #D  
new_pixel_width = new_resolution
new_pixel_height = -new_resolution    #E  

input_width = input_dataset.RasterXSize    #F
input_height = input_dataset.RasterYSize
output_width = int(input_width * (input_geotransform[1] / new_pixel_width))
output_height = int(input_height * (input_geotransform[5] / new_pixel_height))

output_dataset = gdal.GetDriverByName('GTiff').Create(output_path,    #G output_width, output_height, input_dataset.RasterCount, input_dataset.GetRasterBand(1).DataType)

new_geotransform = (    #H
    input_geotransform[0],    #I  
    new_pixel_width,    #J        
    0,    #K                      
    input_geotransform[3],    #L  
    0,    #M                      
    new_pixel_height    #N        
)
output_dataset.SetGeoTransform(new_geotransform)

output_dataset.SetProjection(input_dataset.GetProjection())    #O

gdal.ReprojectImage(input_dataset, output_dataset, None, None, gdal.GRA_Bilinear)    #P

input_dataset = None    #Q
output_dataset = None

print("Resampling complete.")
#A Set the input and output. Remember to replace the input.
#B Open the input raster dataset.
#C Get the input geotransform (spatial transformation metadata).
#D Calculate the new resolution (in meters).
#E Negative because the y-coordinate increases downward.
#F Calculate the new dimensions of the output raster.
#G Create a new raster dataset for the output.
#H Set the new geotransform for the output.
#I X-coordinate of upper-left corner.
#J Pixel width.
#K Rotation (0 if the image is "north-up").
#L Y-coordinate of upper-left corner.
#M Rotation (0 if the image is "north-up").
#N Negative pixel height.
#O Copy the projection information from the input to the output.
#P Perform resampling.
#Q Close the datasets
