user_lat = 40.7128
user_lon = -74.0060
radius = 5 # in kilometers
nearby_restaurants = []
for restaurant in restaurants:
distance = haversine(user_lat, user_lon, restaurant["lat"],
restaurant["lon"])
if distance <= radius:
nearby_restaurants.append(restaurant)
print("Nearby restaurants within a", radius, "km radius:")
for restaurant in nearby_restaurants:
print(restaurant["name"])



