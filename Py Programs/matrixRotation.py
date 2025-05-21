matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

for row in matrix:
    print(row)
print()

n=len(matrix)

for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for row in matrix:
    print(row)
print()        

for i in range (n):
    for j in range(n):
        # matrix[i][j],matrix[n-1-i][j]=matrix[n-1-i][j], matrix[i][j]
        if i>=j:
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp

for row in matrix:
    print(row)
print()