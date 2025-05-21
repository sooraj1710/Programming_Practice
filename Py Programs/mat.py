mat=[] 

for i in range(3):
    row=[]
    for j in range(3):
        row.append(int(input()))
    mat.append(row)

for i in range(3):
    for j in range(3):
        print(mat[i][j],end=" ")
    print()
