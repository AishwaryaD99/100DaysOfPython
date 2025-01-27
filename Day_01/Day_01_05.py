# Exercise 5: Bottle Deposits

rate_one_l = 0.10
more_than_one_l = 0.25

n1 = float(input("Enter the no. of bottles with capacity one litres or less : "))

n2 = float(input("Enter the no. of bottles with capacity with more than 1 litre : "))

amount = round(((n1*rate_one_l)+(n2*more_than_one_l)),2)

print("Your refund amount is : $ ", amount)
