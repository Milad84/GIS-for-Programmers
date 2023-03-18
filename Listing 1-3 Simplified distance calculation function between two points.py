def distance(x1,y1,x2,y2):

#Use any distance formula you want.
# The following is a simplified Euclidean Distance
 
#difference in longitudes
    dx = x2 - x1
#difference in latitudes
    dy = y2 - y1
#Squared summation of lat and long differences
    dsquared = dx*dx + dy*dy
    calculated_distance = dsquared
    return calculated_distance
#Test the result
a = distance(23,45,12,67)
#Print the output
print(a)


