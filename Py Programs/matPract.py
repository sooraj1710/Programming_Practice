n=int (input())

matr=list(map(int,input().split(" ")))
mat=[]
for i in range(0,len(matr),n):
     mat.append(matr[i:i+n])

# new=[[0]*n for i in range(n)]
print(mat)