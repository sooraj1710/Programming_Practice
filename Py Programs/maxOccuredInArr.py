'''def most(arr):
    count=[0,0,0,0,0,0,0]
    n=len(arr)
    for i in range(n):
            count[arr[i]]+=1
        
    return count

arr=[1,1,2,4,3,2,1,6,1]
print(most(arr))
# print(S)'''

arr=[1,1,1,2,3,2,3,4,3,1,2,3]
n=len(arr)
c=[0]*5
for i in range(n):
    c[arr[i]]+=1
print(c)
for i in range(len(c)):
    print(c[i]," ",i)