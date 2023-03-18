
import math

def Trigo_Area(x1,y1,x2,y2):

    calculated_distance_AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    converted_AB_to_kilometers = calculated_distance_AB * 111
    #return converted_AB_to_kilometers

    angle_BZ_AB = 70
    radian=  angle_BZ_AB * 3.14/180
    calculated_AZ =  converted_AB_to_kilometers * math.sin(radian)
    #return calculated_AZ

    calculated_BZ =  converted_AB_to_kilometers * math.cos(radian)
   # return calculated_BZ

    angle_BD_BZ = 45
    radian2 = angle_BD_BZ * 3.14/180
    calculated_ZD = calculated_BZ * math.tan (radian2)
    #return calculated_BD

    calculated_BD =  math.sqrt (calculated_ZD**2 + calculated_BZ**2)

    calculated_AD = calculated_AZ + calculated_ZD

    Area = (1/2 * calculated_AD) * (calculated_BZ)

    print ("AB = ", converted_AB_to_kilometers )
    print ("AZ = ", calculated_AZ )
    print ("BZ = " , calculated_BZ)
    print ("ZD = " , calculated_ZD)
    print ("BD = " , calculated_BD)
    print ("Area = ", Area)

Trigo_Area(-83.27827,37.57490,-82.85313, 37.27827)
