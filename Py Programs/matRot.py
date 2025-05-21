mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(mat)):
    for j in range(len(mat)):
        if i>j:
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

for i in mat:
    print(i)
n=len(mat)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i>=j:
            mat[i][j], mat[i][n-1-j]= mat[i][n-1-j],mat[i][j]
for i in mat:
    print(i) 
