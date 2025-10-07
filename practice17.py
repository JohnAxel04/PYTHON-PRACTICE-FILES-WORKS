

num = eval(input("Put a number limit: "))

sm1 = 0 
sm2 = 0
sm = 0
cn = 0


for i in range(1,num + 1):
    if i % 2 == 0:
        sm += i
        cn += 1
print(f"The sum of even num {sm}")
print(f"The count of even num {cn}")
for i in range(1,num + 1):
    if i % 2 == 1:
        sm1 += i
        sm2 += 1
print(f"The sum of even odd {sm1}")
print(f"The count of even odd {sm2}")



