num = eval(input("Put a number(0 to stop): "))

op = 0
while num != 0:
    print("again")
    num = eval(input("Put a number: "))
    op += num
print(f"The sum of all number is {op}")


