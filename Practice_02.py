print("Grade Calculator")

num = int(input("How many is your Subject? "))

total = 0
count = 1

while count <= num:
    grade = float(input("What grade of it: "))   
    total += grade
    count += 1 
    average = total / num
print(f"average: {average:.2f}")

if average >= 90:
    print("A - Congrats")
elif average >= 80 and average < 90:
    print("B - Goodjob")
elif average >= 70 and average < 80:
    print("C - Nice")
elif average >= 60 and average < 70:
    print("D - Try again")
else:
    print("F - better luck next time ")
