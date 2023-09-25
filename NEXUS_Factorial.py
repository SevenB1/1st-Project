import math
while(True):
     n = int(input("Enter a number: "))
     if n >= 0:
          result = math.factorial(n)
          print(f"The factorial of {n} is {result}.")
          exit()
     else:
          print("Number cannot be less than zero")
