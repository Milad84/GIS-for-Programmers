{
    "$schema": "https://proj.org/schemas/v0.5/projjson.schema.json",
    "type": "GeographicCRS",    #A
    "name": "North_American_1983_3D",
    "datum": {    #B
        “type”: “GeodeticReferenceFrame”,    #B
        "name": "North American Datum 1983",    #B
        "ellipsoid": {    #B
            "name": "GRS 1980",    #B
            "semi_major_axis": 6378137,    #B
            "inverse_flattening": 298.257222101    #B
        }
    },
    "coordinate_system": {
        "subtype": "ellipsoidal",
        "axis": [
            {
                "name": "Geodetic latitude",
                "abbreviation": "Lat",
                "direction": "north",
                "unit": "degree"
            },
            {
                "name": "Geodetic longitude",
                "abbreviation": "Lon",
                "direction": "east",
                "unit": "degree"
            }
        ]
    },
    "scope": "Not known.",
    "area": "North America - onshore and offshore: Canada - Alberta;    #CBritish Columbia; Manitoba; New Brunswick; Newfoundland and Labrador;",
    "bbox": {    #D
        "south_latitude": 14.92,
        "west_longitude": 167.65,
        "north_latitude": 86.45,
        "east_longitude": -40.73
    },
    "id": {
        "authority": "ESRI",
        "code": 104602
    }
}
#A Type of the coordinate system
#B Information about datum
#C Best used for these locations
#D The extent covered by the CRS



