name = input("Whats your name: ")
num = eval(input("put a number of students: "))

print(f"Welcome ma'am {name}")
for i in range(1, num + 1):
    grade = eval(input("put the Grade of the students: "))
    if grade >= 75:
        print(f"You passed {grade}")
    else:
        print(f"Need Improvements {grade}")
print("All students are successfully recorded")






