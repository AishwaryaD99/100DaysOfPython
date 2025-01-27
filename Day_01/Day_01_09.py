# Exercise 9: Compound Interest

interest = 0.04
amt = eval(input("Enter the amount deposited : "))
yr_1 = amt+(interest*amt)
yr_2 = yr_1 + (yr_1*interest)
yr_3 = yr_2 + (yr_2*interest)

print('''Your balance after 1 year is %.2f\nafter 2 years is %.2f\nafter 3 years is %.2f'''%(yr_1,yr_2,yr_3))