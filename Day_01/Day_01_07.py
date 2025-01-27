# Sum of the First n Positive Integers
while True:
  n = int(input("Enter a positive integer: "))

  if n>0:

    sum = n *(n+1)/2
    print("sum is : %d"%sum)
    break 
  
  else :
     print("Invalid input")
     continue  