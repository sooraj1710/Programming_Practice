def solve(arr, tar):
    ans=[]
    n=len(arr)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]

            if sum==tar:
                ans.append(i+1)
                ans.append(j+1)
                return ans
    return[-1]


arr=[1,2,3,4,5]
tar=10
print(solve(arr,tar))

