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
    for j in range(i+1):
            mat[i][j], mat[n-1-i][j]= mat[n-1-i][j],mat[i][j]
print()
for i in mat:
    print(i) 
