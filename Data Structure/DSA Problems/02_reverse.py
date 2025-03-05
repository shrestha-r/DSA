L = [2,3,1,5,9,4]
temp = []
j = len(L)-1
print(j)
for i in range(0,len(L)-1,1):
    temp[i] = L[j]
    j=-1

for i in temp:
    print(temp[i])