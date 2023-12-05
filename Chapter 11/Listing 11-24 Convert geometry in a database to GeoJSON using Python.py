import psycopg2
import geojson
from geojson import FeatureCollection, Feature

conn = psycopg2.connect(    #A
    database="postgres",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5433"
)

cursor = conn.cursor()    #B

cursor.execute("SELECT id, ST_AsGeoJSON(geom)::json AS geometry FROM ch01.restaurants;")    #C

rows = cursor.fetchall()    #D

cursor.close()
conn.close()

features = []    #E

for row in rows:
    feature = {
        "type": "Feature",
        "properties": {
            "id": row[0]
        },
        "geometry": row[1]
    }
    features.append(feature)

feature_collection = FeatureCollection(features)

geojson_string = geojson.dumps(feature_collection, indent=2)    #F

print(geojson_string)

output_file = "D:/outputCh11.geojson"    #G  
with open(output_file, "w") as geojson_file:
    geojson_file.write(geojson_string)

print(f"GeoJSON data saved to {output_file}")

#A Connect to the PostgreSQL database
#B Create a cursor object
#C Execute the SQL query 
#D Fetch all the results
#E Create a GeoJSON FeatureCollection
#F Convert the FeatureCollection to GeoJSON string
#G Save the GeoJSON data to a file
