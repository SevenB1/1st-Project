balance = 1000
secretcode = "1234"
print("\t\t\t -------- WELCOME TO ATM PROGRAM -------------")
pincode = input("Please enter the pincode: ")
if pincode == secretcode:
    print("Pincode verification is successful")
else:
    print("ERROR: Invalid Pincode")
    exit()
while(True):    
    print("\t\t\t ========== ATM MENU ============")
    print("\t\t\t 1. CASH WITHDRAWAL")
    print("\t\t\t 2. CASH DEPOSIT")
    print("\t\t\t 3. CHECK BALANCE")
    print("\t\t\t 4. EXIT")

    option = input("SELECT THE OPTION: ")
    if option == "1":
        amount = int(input("Enter the amount: "))
        if amount <= balance:
            balance = balance - amount
            print(f"Please collect your cash worth {amount} Rupees") 
        else:
            print("Insufficient Balance")
    elif option == "2":
        amount = int(input("Enter the Amount to Deposit "))
        if amount < 500:
            print("Please Deposit the Amount > 500 Rs")
            exit()
        else:
            print("Successfull: Your Current Balance is", balance + amount )
    elif option == "3":
        print (balance)
    elif option == "4":
        exit()
    else:
        print("ERROR: Invalid syntax")
        exit()
    cont_opt = input("Would you like another transaction (y/n) ?")
    if cont_opt == "n" or "N":
        exit()
    elif cont_opt == "y" or "Y":
        continue
    else:
        print("EEROR: You have Selected the wrong option: Exiting the program")
        exit()