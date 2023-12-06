SELECT ST_Distance(    #A
  'SRID=3857;POINT(-118.4079 33.9434)'::geometry,    #B
  'SRID=3857;POINT(2.5559 49.0083)'::geometry    #C     
  );
#A ST_Distance is the function used to calculate the distance between features
#B Coordinates of Los Angeles cast as a geometry
#C Coordinates of Paris cast as a geometry
