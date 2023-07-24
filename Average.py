from statistics import mean

A = int(input("Number of values:"))

if A == 2:
    a = int(input("What's x?"))
    b = int(input("What's y?"))
    print(mean([a, b]))
elif A == 3:
    a = int(input("What's x?"))
    b = int(input("What's y?"))

else:
    print("Code not sufficent")