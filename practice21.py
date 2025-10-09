#Number triangle with real squares
num = int(input("Put a number: "))

va = 1
for me in range(2,6):
    for n in range(1,me):
        print(f"{va ** 2}",end=" ")
        va += 1
    print()