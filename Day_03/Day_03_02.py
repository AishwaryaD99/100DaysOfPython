# Exercise 19: Free Fall
from math import sqrt
d = float(input("Enter height from which object is dropped : "))

u = 0
a = 9.8
v = sqrt(u+(2*a*d))

print("The speed at which the object fell is : %.2f m/s "%v)


