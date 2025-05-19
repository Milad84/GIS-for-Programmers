import pyproj
import matplotlib.pyplot as plt

def compare_coordinate_systems(point):
    utm_projection = pyproj.Proj(proj='utm', zone=10, ellps='WGS84')    #A
    wgs84_projection = pyproj.Proj(proj='latlong', datum='WGS84')    #B

    lon, lat = pyproj.transform(utm_projection, wgs84_projection, point[0], point[1])    #C

    print(f"UTM coordinates: {point[0]}, {point[1]}")
    print(f"WGS84 coordinates: {lon}, {lat}")

    plt.plot(point[0], point[1], 'bo', label='UTM')
    plt.plot(lon, lat, 'ro', label='WGS84')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.title('Comparison of Point Positions')
    plt.grid(True)
    plt.show()

point_in_utm = (500000, 4500000)    #D
compare_coordinate_systems(point_in_utm)

#A Define the UTM projection (UTM zone 10N)
#B Define the WGS84 projection
#C Transform the point from UTM to WGS84
#D UTM coordinates (eastings, northings) to test the function

