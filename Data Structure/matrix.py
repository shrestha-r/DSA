row = int(input("how many row? "))
column = int(input("how many column? "))

matrix = [[0]*column]*row

for i in range(row):
    for j in range(column):
        matrix[i][j] = int(input(f"value for {i+1} X {j+1}: "))

for i in range(row):
    for j in range(column):
        print(f'{matrix[i][j]}---',end="")
    print()