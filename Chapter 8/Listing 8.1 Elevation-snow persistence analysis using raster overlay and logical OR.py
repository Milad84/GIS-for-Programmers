import numpy as np

elevation_raster = np.array([[100, 200, 300],    #A
                             [400, 500, 600],
                             [700, 800, 900]])

snow_cover_raster = np.array([[False, False, True],
                              [True, True, False],
                              [False, True, True]])

elevation_threshold = 500    #B

snow_persistent = np.logical_or(snow_cover_raster, elevation_raster >= elevation_threshold)    #C

print("Snow Persistence Raster:")
print(snow_persistent)
#A Simulated elevation and snow cover raster data (arrays)
#B Define elevation threshold for snow persistence 
#C Apply logical OR operation to determine where snow persists at the given elevation

