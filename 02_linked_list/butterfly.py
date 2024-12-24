
row =5
column = 10
n = 5
for i in range(n):
    for i in range(1,i):
        print("*",end="")
    for j in range(1,column-(i*2)):
        print(" ",end="")
    for l in range(1,i):
        print("*",end="")
    print("\n")

    