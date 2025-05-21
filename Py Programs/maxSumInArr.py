arr=[2,3,-8,7,-1,2,3]
max=-100000000000000
n=len(arr)
'''for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        if sum>max:
            max=sum
print(max)'''

for i in range(n):
    sum=0
    for j in range(i,n):
        sum=sum+arr[j]
        if sum>max:
            max=sum
            
print(max)