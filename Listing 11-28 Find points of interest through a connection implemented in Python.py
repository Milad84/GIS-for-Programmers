import psycopg2
from geojson import Point

db_params = {    #A
    "host": "localhost",
    "database": "YOUR_DATABSE",
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    'port': 5433,
}

try:
    
    lat = float(input("Enter latitude: "))    #B
    lon = float(input("Enter longitude: "))
    radius = float(input("Enter radius in meters: "))

    user_location = Point((lon, lat))    #C

    conn = psycopg2.connect(**db_params)    #D

    cursor = conn.cursor()    #E

    query = """    #F
        SELECT id, wkb_geometry
        FROM public.respoints
        WHERE ST_DWithin(
            wkb_geometry::geography,
            ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
            %s
        )
    """
    cursor.execute(query, (lon, lat, radius))

    results = cursor.fetchall()    #G

    features = []    #H
    for row in results:
        feature = {
            'type': 'Feature',
            'properties': {
                'id': row[0],
            },
            'geometry': row[1]
        }
        features.append(feature)

    geojson_response = {
        'type': 'FeatureCollection',
        'features': features
    }

    print(geojson_response)

    cursor.close()
    conn.close()

except Exception as e:
    print(str(e))
#A Database connection parameters
#B Get user input for latitude, longitude, and radius
#C Create a Point object from the user's location
#D Establish a database connection
#E Create a cursor
#F Perform the spatial query
#G Fetch results
#H Convert the results to GeoJSON format

