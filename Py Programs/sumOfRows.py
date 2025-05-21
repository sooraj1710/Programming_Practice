mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]

sum=0
res=[]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        sum+=mat[i][j]
    res.append(sum)
max=-1
for i in range(len(res)):
    if(res[i]>max):
        max=res[i]
        m=i+1

print(m)