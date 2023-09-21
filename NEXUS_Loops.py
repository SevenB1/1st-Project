while(True):
    print("\t\t\t ============ AREA CALCULATOR ============")
    print("1. Area of Circle")
    print("2. Area of Square")
    print("3. Area of Rectangle")
    print("4. Area of Triangle")
    print("5. Area of Cylinder")

    option = int(input("Select any of the above options: "))

    if option == 1:
        radius = int(input("Enter the radius: "))
        area = 3.14 * radius ** 2
        print(f"The Area of Circle with radius {radius} is {area}")
    elif option == 2:
        side_length = int(input("Enter the Side Length: "))
        area = side_length ** 2
        print(f"The Area of a Square with Side Length {side_length} is {area}")
    elif option == 3:
        heigth = int(input("Enter the Heigth: "))
        width = int(input("Enter the Width: "))
        area = heigth * width
        print(f"The Area of Rectangle with Heigth {heigth} and Width {width} is {area}")
    elif option == 4:
        base_length = int(input("Enter the Base Length: "))
        heigth = int(input("Enter the Heigth: "))
        area = 1/2 * base_length * heigth
        print(f"The Area of Triangle with Base Length {base_length} and Heigth {heigth} is {area}")
    elif option == 5:
        radius = int(input("Enter the radius: "))
        heigth = int(input("Enter the Heigth: "))
        area = 2 * 3.14 * radius * (radius + heigth)
        print(f"The Area of a Cylinder with Radius {radius} and Heigth {heigth} is {area}")
    else:
        print("Please pick options from above")    
    repeat = input("If you would like to do another function enter Y: ")
    if repeat == "y" or repeat == "Y":
        continue
    else:
        exit()