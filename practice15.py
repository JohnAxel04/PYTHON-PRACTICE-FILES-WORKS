name = input("Whats your name: ")
num = eval(input("put a number of subjects: "))

total = 0

for i in range(1,num + 1):
    subj = input(f"Name of the Subject {i}: ")
    grade = eval(input("What grade of that subject? "))
    total += grade

average = total / num

if average >= 75:
    new = "passed"
else:
    new = "failed"

print(f"Name of the Student {name}")
print(f"Average: {average:.2f}")
print(f"You {new}")





