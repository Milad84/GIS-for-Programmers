SELECT ST_Distance(
  'SRID=4326;POINT(-118.4079 33.9434)'::geography, 
  'SRID=4326;POINT(2.5559 49.0083)'::geography     
  );
