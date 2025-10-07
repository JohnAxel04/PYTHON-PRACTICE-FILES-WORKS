for me in range(1,6):
    for n in range(6,me,-1):
        print(" ",end="")
    for i in range(1,me+1,1):
        print(i,end="")
    for u in range(me - 1,0,-1):
        print(u,end="")
    print()
for p in range(5 - 2,0 - 1, -1):
    for t in range(5,p,-1):
        print(" ",end="")
    for e in range(1 , p + 2, 1):
        print(e,end="")
    for tm in range(1,p + 1,1):
        print(tm,end="")
    print()

