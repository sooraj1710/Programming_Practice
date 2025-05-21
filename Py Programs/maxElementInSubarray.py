arr=[1,-3,5,6,7,3,-1]
n=len(arr)
k=3
res=[]
for i in range(n):
    res.append(max(arr[i:i+k]))
print(res[0:n-1])
