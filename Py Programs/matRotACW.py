'''matrix=[[1,2,3],
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
        if i<=j:
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-i][j]
            matrix[n-1-i][j] = temp

for row in matrix:
    print(row)
print()'''

def rot(mat):
    n=len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    
    for i in range(n):
        for j in range(i):
            mat[i][j],mat[n-i-1][j]=mat[n-i-1][j],mat[i][j]
    return mat

mat=[[1,2,3],
        [4,5,6],
        [7,8,9]]
s=rot(mat)
for i in range(len(s)):
    print(s[i])
