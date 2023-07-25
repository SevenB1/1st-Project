def main():
    x = get_int("Why x?")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please give an integer")
        
main()