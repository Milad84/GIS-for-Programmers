from pyproj import Transformer

pipeline_str = ("+init=ITRF2008:ITRF2000")

pipe_trans = Transformer.from_pipeline(pipeline_str)
for pt in pipe_trans.itransform([(35000, 74000)]):
    print (pt)
