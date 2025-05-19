from math import radians, cos, sin, sqrt

def calculate_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])    #A

    earth_radius = 6371.0    #B

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2    #C
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = earth_radius * c

    return distance

lat1, lon1 = 40.7128, -74.0060  # New York City coordinates
lat2, lon2 = 34.0522, -118.2437  # Los Angeles coordinates

distance = calculate_distance(lat1, lon1, lat2, lon2)
print(f"The distance between New York City and Los Angeles is approximately {distance} km.")
#A Convert degrees to radians 
#B Earth's radius in kilometers
#C Haversine formula for distance calculation
