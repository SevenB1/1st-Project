name = input("What's your name?")


with open("Names.txt", "a", ) as file:
    file.write(f"{name}\n")
