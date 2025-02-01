# Exercise 18:Volume of a Cylinder

from  math import pi 

r ,h = input("Enter the radius and height separated by commas : ").split(",")
r = int(r)
h = int(h)
vol = pi* r * h
print("volume = %.2f"%vol)
