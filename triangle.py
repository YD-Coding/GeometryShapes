# from math import sin, radians
# class Traingle:
#     def __init__(self, base, rib2, rib3, angle1, angle2):
#         self.base = base
#         self.rib2 = rib2
#         self.rib3 = rib3

#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = 180 - angle2 - angle1

#         self.height = self.base * self.rib2 * sin(radians(self.angle3)) / 2

def isFloat(number):
    if float(number) == int(number):
        return int(number)
    return("{:.2f}".format(number))

#print(isFloat(5.00))