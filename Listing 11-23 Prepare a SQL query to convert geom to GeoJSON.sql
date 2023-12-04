SELECT id, ST_AsGeoJSON(geom)::json AS geometry
FROM your_table_name;
