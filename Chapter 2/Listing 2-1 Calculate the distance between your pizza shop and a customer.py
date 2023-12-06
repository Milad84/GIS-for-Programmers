import requests

api_key = 'Your Google Maps API'    #A

start_coordinates = '37.7749,-122.4194'  
destination_coordinates = '36.0522,-119.2437'    #B

url =    #C f'https://maps.googleapis.com/maps/api/directions/json?origin={start_coordinates}&destination={destination_coordinates}&mode=driving&key={api_key}'
response = requests.get(url)
data = response.json()

if 'routes' in data and len(data['routes']) > 0:    #D
    route = data['routes'][0]

    if 'legs' in route and len(route['legs']) > 0:
        leg = route['legs'][0]

        duration_text = leg['duration']['text']    #E  
        duration_seconds = leg['duration']['value']    #F  

        print(f"Drive Time from {start_coordinates} to {destination_coordinates}:")
        print(f"Duration: {duration_text}")
        print(f"Duration in Seconds: {duration_seconds}")
else:
    print("No route found.")
#A Replace with your Google Maps API key
#B Replace with your starting and destination coordinates (latitude, longitude)
#C Make the request
#D Extract drive time information 
#E Drive time as a human-readable string
#F Duration in seconds
