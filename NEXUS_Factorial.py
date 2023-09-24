import math
n = int(input("Enter a number: "))
if n >= 1:
     result = math.factorial(n)
     print(result)
else:
     print("Number cannot be less than zero")
