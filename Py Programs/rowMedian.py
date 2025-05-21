n=int(input("enter order of matrix: "))
matrix=[]
for i in range(n):
    arr=list(map(int,input().split(" ")))
    matrix.append(arr)

def median(arr):
    arr.sort()
    n=len(arr)
    if len(arr)%2==0:
        n1=arr[n//2]
        n2=arr[(n//2) -1]
        return (n1+n2)/2
    else:
        return arr[n//2]

for i in matrix:
    ans=median(i)
    print(ans)