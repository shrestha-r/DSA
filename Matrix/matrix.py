

matrix_a = [[1,2,3,4,5],[6,7,8,9,10]]
matrix_b = [[11,12,13,14,15],[16,17,18,19,20]]

matrix = [[]]*2
print(matrix)
for i in range(2):
    ans = []
    for j in range(5):
        ans.append(matrix_a[i][j] + matrix_b[i][j])
    matrix[i].append(ans)

print(matrix)