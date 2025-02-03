# s1 = float(s1)
from math import sqrt
s1,s2,s3 = input("Enter the sides of the triangle : ").split(",")

s1 = float(s1)
s2 = float(s2)
s3 = float(s3)
s = s1+s2+s3

area = sqrt(s * (s-s1)*(s-s2)*(s-s3))

print("area od triangle is : %.f"%area)