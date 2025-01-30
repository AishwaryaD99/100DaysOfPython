# Exercise 15: Distance Units

feet = int(input("Enter distancce in inches, yards and miles : "))


inches = feet * 12
yards = feet * 0.333
miles = yards * 0.0005681818

print('''distance in inches is %.2f,\nin yards - %.2f,\nin miles - %.2f  '''%(inches,yards,miles))