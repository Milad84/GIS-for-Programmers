import math

def trigo():

    side1 = 0
    side2 = 0
    side3 = 0
    angle_S1_S2 = 0
    angle_S2_S3 = 0
    angle_S3_S1 = 0

    angle_S1_S2 = 32
    side1 = 5
    side2 = 8
    radian=  angle_S1_S2 * 3.14/180
    side3 = math.sqrt ((side1**2 + side2**2)-2*(side1*side2)* math.cos(radian))
    print(side3)

trigo()
