# Exercise 14: Making Change

h_feet = int(input("Enter height in feet  : "))
h_inches = int(input("Enter height in inches  : "))

tot_inches = (h_feet*12)+ h_inches
cms = tot_inches*2.54

print("The height in cms is %.2f : "%cms)
