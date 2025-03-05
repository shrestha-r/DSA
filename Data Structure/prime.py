list = []
for i in range(100):
    if i>1:
        for j in range(2,i):
            if i %j == 0:
                break
    print(i)
print(list)