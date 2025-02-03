# Exercise 23: Area of a Regular Polygon
from math import tan,pi
s, n = input("Enter the length of side and no. of sides : ").split(',')
s = float(s)
n = float(n)
area = ((s**2) * n) /(4*tan(pi/n))

print("The area of polygon = %.2f"%area)

