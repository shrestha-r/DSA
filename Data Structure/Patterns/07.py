row = 6
column = 100
for i in range(0,row):
    for j in range(0,int((column - (i+1)*2)/2)):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    for l in range(0,int((column - (i+1)*2)/2)):
            print(" ",end="")
    print()

