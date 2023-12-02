def distance(x1,y1,x2,y2):
    dx = x2 - x1    #A
    dy = y2 - y1    #B
    dsquared = dx*dx + dy*dy    #C
    calculated_distance = dsquared
    return calculated_distance
a = distance(23,45,12,67)
print(a)    #D
#A Difference in longitudes
#B Difference in latitudes
#C Squared summation of lat and long differences
#D Check the distance between two points in an imaginary unit



