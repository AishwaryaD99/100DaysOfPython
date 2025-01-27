# Exercise 10: Arithmetic
from math import log10 
while True: 
 a = int(input("Enter an integer : "))
 b = int(input("Enter second integer : "))
 if a>0 and b>0 :
    sum = a+b
    diff = a-b
    product = a*b
    quo = a%b
    rem = a//b
    log = log10(a)
    power = a**b

    print("The sum of %a and %a is : %a "%(a,b,sum))
    print("The difference when %a is subtracted from %a is : %a "%(a,b,diff))
    print("The product of %d and %d is : %d "%(a,b,product))
    print("The quotient when %a is divided by %a is : %.2f"%(a,b,quo))
    print("The remainder when %a is divided by %a is : %a "%(a,b,rem))
    print("The result of log10 %a is %2.f"%(a,log)) 
    print("The result of %a^%a is : %a"%(a,b,power))
    break
 else:
   print("Invalid integers")
