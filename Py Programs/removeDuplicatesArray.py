arr=[1,2,2,5,1,3,4,5,7,6,7,5,10,10,12]

res=[]

for i in range(len(arr)):
    if arr[i] not in res:
        res.append(arr[i])
print(res)