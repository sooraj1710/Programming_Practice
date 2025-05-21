'''n=int(input())
k=int(input())
a=list(map(int,input().split(" ")))
max=0

for i in range(0, len(a)):
    sum=a[i]
    for j in range(i+1, len(a)):
        sum=sum+a[j]
        if sum==k:             
            if(max< j-i):
                max=j-i
                start=i
        elif sum>k:
            i+=1

print(start)'''
arr=list(map(int,input("enter arr: ").split(" ")))
k=int(input("enter key: "))
s=[]
e=[]
r=[]
n=len(arr)
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        if sum==k:
            print(i,j)
            s.append(i)
            e.append(j)

for i in range(len(s)):
    r.append(e[i]-s[i])
l=r.index(max(r))
print(s[l])
        