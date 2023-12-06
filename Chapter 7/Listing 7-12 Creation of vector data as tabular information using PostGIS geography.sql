create schema test;

CREATE TABLE test.table2 
(id char(3) PRIMARY KEY
 , name varchar(30)
 , geog geography(point, 4326)); 

INSERT INTO test.table2(id, name, geog) 
VALUES 
  ('ABC', 'Dana', ST_Point(34.4, 45.2)), 
  ('DEF', 'Robert', ST_Point(-36.4, 69.2)),
  ('GHI', 'Curtis', ST_Point(33.5, 56.2));

select * from test.table2;
