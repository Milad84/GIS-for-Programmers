SELECT id, wkb_geometry
FROM public.respoints
WHERE ST_DWithin(
    wkb_geometry::geography,
    ST_SetSRID(ST_MakePoint(-77.985130, 38.748817), 4326)::geography, -- Replace with your coordinates
    500000 -- Search radius in meters
);

