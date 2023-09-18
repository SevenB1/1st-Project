print(" ========== SIMPLE CALCULATOR ========== ")
print("1.Division")
print("2.Multiplication")
print("3.Addition")
print("4.Subraction")
print("5.Floor Division")
print("6.Power")
print("7.Remainder")

format = float(input("Enter the desired format: "))
if format == 1:
    a = float(input("Enter the Numerator: "))
    b = float(input("Enter the Denominator: "))
    c = a / b 
    print(f"{a}/{b} = {round(c, 2)}")
elif format == 2:
    a = float(input("Enter the Multiplicand: "))
    b = float(input("Enter the Multiplier: "))
    c = a * b 
    print(f"{a}*{b} = {round(c, 2)}")
elif format == 3:
    a = float(input("Enter the First Number: "))
    b = float(input("Enter the Second Number: "))
    c = a + b 
    print(f"{a}+{b} = {round(c, 2)}")
elif format == 4:
    a = float(input("Enter the Minuend: "))
    b = float(input("Enter the Subtrahend: "))
    c = a - b 
    print(f"{a}-{b} = {round(c, 2)}")
elif format == 5:
    a = float(input("Enter the Numerator: "))
    b = float(input("Enter the Denominator: "))
    c = a // b 
    print(f"{a}//{b} = {c}")
elif format == 6:
    a = float(input("Enter the Base: "))
    b = float(input("Enter the Exponent: "))
    c = a ** b 
    print(f"{a}^{b} = {round(c, 2)}")
elif format == 7:
    a = float(input("Enter the Dividend: "))
    b = float(input("Enter the Divisor: "))
    c = a % b 
    print(f"{a}%{b} = {round(c, 2)}")
else:
    print("Please choose an operation from above.")