# Exercise 6:Tax and Tip

cost = eval(input("Enter the cost of meal : "))

tax = 0.12
tip = 0.18

tax_amnt = cost*tax
tip_amnt = cost*tip
total = cost + tip_amnt + tax_amnt

print('''Tax is = %.2f\nTip is = %.2f\nTotal = %.2f''' % (tax_amnt,tip_amnt,total))
