from osgeo import ogr

driver = ogr.GetDriverByName("ESRI Shapefile")    #A

output_path = "D:\output.shp"
shapefile = driver.CreateDataSource(output_path)

layer_name = "my_layer"    #B
layer = shapefile.CreateLayer(layer_name, geom_type=ogr.wkbPolygon)

field_name = ogr.FieldDefn("Name", ogr.OFTString)    #C
field_name.SetWidth(50)
layer.CreateField(field_name)

polygon = ogr.Geometry(ogr.wkbPolygon)    #D
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(0, 0)
ring.AddPoint(1, 0)
ring.AddPoint(1, 1)
ring.AddPoint(0, 1)
ring.AddPoint(0, 0)
polygon.AddGeometry(ring)
feature = ogr.Feature(layer.GetLayerDefn())    #E
feature.SetGeometry(polygon)
feature.SetField("Name", "My Polygon")
layer.CreateFeature(feature)

feature = None
shapefile = None
#A Set up the shapefile driver
#B Create a new layer in the shapefile object
#C Define attribute fields for the layer
#D Create a polygon feature
#E Create a new feature in the layer
