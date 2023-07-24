# This code can be used to find the average between some numbers given by the user.

from statistics import mean

A = int(input("Number of values:"))

if A == 2:
    a = int(input("What's the 1st value? "))
    b = int(input("What's the 2nd value? "))
    print("The Average is", mean([a, b]))
elif A == 3:
    a = int(input("What's the 1st value? "))
    b = int(input("What's the 2nd value? "))
    c = int(input("What's the 3rd value? "))
    print("The Average is", mean([a,b,c]))
elif A == 4:
    a = int(input("What's the 1st value? "))
    b = int(input("What's the 2nd value? "))
    c = int(input("What's the 3rd value? "))
    d = int(input("What's the 4th value? "))
    print("The Average is", mean([a,b,c,d]))    
else:
    print("Code not sufficent")