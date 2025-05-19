user_lat = 40.7128
user_lon = -74.0060
radius = 5  # in kilometers

# Sample list of restaurants with their coordinates
restaurants = [
    {"name": "McDonalds", "lat": 40.7138, "lon": -74.0065},
    {"name": "Chick-fil-A", "lat": 40.7188, "lon": -74.0050},
    {"name": "Burger King", "lat": 40.7028, "lon": -74.0100},
    {"name": "Panda Express", "lat": 40.7288, "lon": -74.0000},
]

nearby_restaurants = []

for restaurant in restaurants:
    distance = haversine(user_lat, user_lon, restaurant["lat"], restaurant["lon"])
    if distance <= radius:
        restaurant["distance"] = distance  # Add distance to the restaurant dictionary
        nearby_restaurants.append(restaurant)

# Print the output
print(f"Nearby restaurants within a {radius} km radius:")
for restaurant in nearby_restaurants:
    print(f"{restaurant['name']} - {restaurant['distance']:.2f} km")

print("\nFeel free to modify the user coordinates, radius, and restaurant data to see how the results change. This will help you understand how the Haversine formula works and verify your implementation.")


