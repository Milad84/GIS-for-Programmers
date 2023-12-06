select path '[(2,2),(3,3),(4,4)]';    #A
select area (box '(2,2),(0,0)');    #B
select lseg '[(0,0),(1,1)]';    #C
select length(path '((-1,0),(1,0))');    #D
select npoints(path '[(0,0),(1,1),(2,0), (-4,-5)]');    #E
