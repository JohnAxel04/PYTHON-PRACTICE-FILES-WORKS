#Mulitplication table using for nested loop

for i in range(1,4):
    print(f"Multiplication for {i}")
    for u in range(1,i + 1): 
        print(f"{i} x {u} = {i * u}") #answer become the output
    print()