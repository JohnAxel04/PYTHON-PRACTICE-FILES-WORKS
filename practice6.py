num = eval(input("Put a Grade(0-100): "))

if num >= 90:
    print("Excellent")
elif num >= 75 and num < 90:
    print("Good job")
elif num < 75:
    print("Need Improvement")
else:
    print("Error Try Again")
