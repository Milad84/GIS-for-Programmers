import math

def Trigo():

    Side1 = 0
    Side2 = 0
    Side3 = 0
    angle_S1_S2 = 0
    angle_S2_S3 = 0
    angle_S3_S1 = 0

    angle_S1_S2 = 32
    Side1 = 5
    Side2 = 8
    radian=  angle_S1_S2 * 3.14/180
    Side3 = math.sqrt((Side1**2 + Side2**2)-2*(Side1*Side2) * math.cos(radian))
    print(Side3)

Trigo()