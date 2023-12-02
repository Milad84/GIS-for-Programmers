from pyproj import Transformer

transproj = Transformer.from_crs(
    "EPSG:4328",
    "EPSG:4326",
   always_xy=True,
)
for pt in transproj.itransform(
    [(-2704026.010, -4253051.810, 3895878.820)],
    radians=True,
):
    print (pt)
