import requests

api_key = 'INSERT YOUR API KEY HERE'    #A

start_coordinates = '37.7749,-122.4194'
destination_coordinates = '36.0522,-119.2437'    #B

url = (
    f'https://maps.googleapis.com/maps/api/directions/json?origin={start_coordinates}&destination={destination_coordinates}&mode=driving&key={api_key}'
)    #C

response = requests.get(url)
data = response.json()

if 'routes' in data and len(data['routes']) > 0:    #D
    route = data['routes'][0]

    if 'legs' in route and len(route['legs']) > 0:    #E
        leg = route['legs'][0]

        duration_text = leg['duration']['text']
        duration_seconds = leg['duration']['value']    #F

        distance_text = leg['distance']['text']    #G
        distance_meters = leg['distance']['value']

        distance_miles = distance_meters * 0.000621371    #H

        print(f"Drive Time from {start_coordinates} to {destination_coordinates}:")
        print(f"Duration: {duration_text}")
        print(f"Duration in Seconds: {duration_seconds}")
        print(f"Distance: {distance_text}")
        print(f"Distance in Miles: {distance_miles:.2f}")

else:
    print("No route found.")
