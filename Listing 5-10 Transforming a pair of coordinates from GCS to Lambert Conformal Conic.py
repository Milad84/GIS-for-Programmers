from pyproj import Transformer

ProjectTo = ("+proj=lcc +lat_1=20 +lat_2=60 lon_0=-100 +datum=NAD83 +units=m")
Tran = Transformer.from_pipeline(ProjectTo)
for pt in Tran.itransform([(45, 36)]):
    print (pt)
