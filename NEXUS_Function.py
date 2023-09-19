def cube(x):
    return x ** 3
def square_area(x):
    return x ** 2
def rect_area(length,width):
    return length * width
while(True):
    print('\t\t\t============ 1. Find the Cube              ===============')
    print('\t\t\t============ 2. Find the area of Square    ===============')
    print('\t\t\t============ 3. Find the area of Rectangle ===============')
    option = input('Please Enter the option: ')
    if option == '1':
        number = int(input('Please Enter the number to find the cube: '))
        y = cube(number)
        print(f'The cube of {number} is {y}')
    elif option == '2':
        side = int(input('Please Enter the side length of square in meters: '))
        area = square_area(side) 
        print(f'The Area of Square with side length {side} meters is {area} sq.meters')
    elif option == '3':
        length = int(input('Please Enter the length of rectangle in meters: '))
        width = int(input('Please Enter the width of rectangle in meters: '))
        area = rect_area(length,width) 
        print(f'The Area of Rectangle with length {length} meters and width {width} meters is {area} sq.meters')
    else:
        exit()
    repeat = input("Would you like to do another process (y/n)? ")
    if repeat == "y" or repeat == "Y":
        continue
    elif repeat == "n" or repeat == "N":
        exit()
    else:
        exit()