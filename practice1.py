print("WELCOME TO ATM BANK")
print("You have 1000 pesos")
print("Select: \n1 - Deposit \n2 - Withdraw \n3 - Check_blnc \n4 - Exit\n")
num = int(input("Enter Your Choice: "))
print("-----------------------")
bl = 1000

while num != 4:

    if num == 1:
        print("*Deposit*")
        ac = int(input("How much you will deposit: "))
        bl +=ac
        print(f"You deposited: {ac}")
        print(f"New Balance: {bl}")
    elif num == 2:
        print("*Withdraw*")
        wd = int(input("How much You will withdraw: "))
        if wd <= bl:
            bl -= wd
            print(f"You widthdraw: {wd}")
            print("Balance left: ",bl)
        else:
            print("Balance not enough")
    elif num == 3:
        print("*Balance*")
        print("\n-----------------------")
        print(f"Balance: {bl}")
    else:
        print("Invalid Choice")
    print("\n-----------------------")
    num = int(input("Enter You Choice: "))
print("\nThank you")