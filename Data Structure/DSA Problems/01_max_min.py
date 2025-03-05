

L = [2]
min = L[0]
max = L[0]
if len(L) == 1:
        print("min and max both is same i.e ",min,"because list has only one item.")
else:
     
    for i in range(1,len(L)):
        if min > L[i]:
            min = L[i]
        if max < L[i]:
            max = L[i]
    print("max is ", max)
    print("min is ", min)