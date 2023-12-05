ndvi = image.normalizedDifference(['B5', 'B4'])    #A

Image(url=ndvi.getThumbUrl({'min': -1, 'max': 1, 'palette': ['blue', 'white', 'green']}))    #B
#A Calculate NDVI for the selected image
#B Visualize the result
