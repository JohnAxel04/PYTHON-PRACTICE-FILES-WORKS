num = eval(input("Put a Number: "))
nim = eval(input("Put a Number: "))
nam = eval(input("Put a Number: "))

low = 0

if num < nim and num < nam:
    low += num
elif nim < num and nim < nam:
    low += nim
elif nam < num and nam < nim:
    low += nam
    
print(low)






