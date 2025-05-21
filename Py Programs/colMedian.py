n=int(input("enter n:"))
matrix=[]
for i in range(n):
    arr=list(map(int,input().split(" ")))
    matrix.append(arr)

def med(arr):
    arr.sort()
    n = len(arr)
    if n%2==0:
        n1=arr[n//2]
        n2=arr[n//2 - 1]
        return (n1+n2)/2
    
    else:
        return arr[n//2]

def transpose(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i>j:
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    return mat

transpose(matrix)
for i in range(len(matrix)):
    print(med(matrix[i]))
