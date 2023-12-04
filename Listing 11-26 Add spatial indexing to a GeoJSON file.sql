CREATE INDEX rspoints_geom_idx ON respoints USING GIST (wkb_geometry);
