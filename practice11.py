sc = 4

num = eval(input("Guess the number(1 to 10): "))

while num != 4:

    if num < 4 and num > 0: 
        print("Too low guess again")
    elif num > 4 and num <= 10:
        print("Too high guess again")
    else:
        print("Error Try again")
    num = eval(input("Guess the number(1 to 10): "))
print(f"\nYou guessed right the number is {sc}")
       





