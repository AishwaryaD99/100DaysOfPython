# Exercise 12: Distance Between Two Points on Earth

from math import sin,acos,cos,radians

t1,g1 = (input("Enter 1st coordinates separated by comma: ")).split(",", 1)

t2,g2 = (input("Enter 2nd coordinates separated by comma: ")).split(",", 1)
t1 = int(t1)
t2 = int(t2)
g1 = int(g1)
g2 = int(g2)

distance = 6371.01 * acos(sin(radians(t1)))+sin(radians(t2))+ (cos(radians(t1)) * cos(radians(t2))*cos((radians(g1)-radians(g2))))

print("distance in km = %.2f"%(distance))
