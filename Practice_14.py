name = input("Whats your name: ")
num = eval(input("put a number of students: "))

pas = 0
fail = 0
print(f"Welcome ma'am {name}")
for i in range(1, num + 1):
    grade = eval(input("put the Grade of the students: "))
    if grade >= 75:
        print(f"You passed {grade}")
        pas += 1
    else:
        print(f"Need Improvements {grade}")
        fail += 1
print("All students are successfully recorded")
print(f"Students pass grade {pas}")
print(f"Students fail grade {fail}")






