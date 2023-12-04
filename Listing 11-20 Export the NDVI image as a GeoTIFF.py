import geemap
import requests
from io import BytesIO

export_params = {    #A
    'image': ndvi,
    'description': 'ndvi_export',
    'region': roi,
    'scale': 30,
    'fileFormat': 'GeoTIFF',  # Specify the file format
}

download_url = export_params['image'].getDownloadURL(export_params)    #B

response = requests.get(download_url)    #C
image_content = BytesIO(response.content)

with open('/content/ndvi_export.tif', 'wb') as file:    #D
    file.write(image_content.getvalue())
#A Define the export parameters
#B Get the download URL for the image
#C Use requests to download the image to your Colab environment
#D Save the image to your Colab environment
