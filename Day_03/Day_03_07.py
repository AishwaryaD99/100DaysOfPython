# Exercise 24: Units of Time


d,h,m,s = input("Enter the days,hours,minutes,seconds separated by ':' - ").split(':')
s= int(s)
m = int(m)*60
h = int(h)*60*60
d = int(d)*60*60*24
total_seconds = s+m+h+d
print("The total no. of seconds =  ",total_seconds)