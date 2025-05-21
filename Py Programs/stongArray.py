'''def fact(m):
    f=1
    if m==0 or m==1:
        return 1
    else:
        for i in range(1,m+1):
            f=f*i
        return f


def strong(n):
    sum=0
    temp=n
    while(n>0):
        dig=n%10
        sum+=fact(dig)
        n//=10
    if(temp==sum):
        return True
    return False

b=[]
a=[2, 4,89,145,40585]
for i in range(len(a)):
    m=strong(a[i])
    if(m==True):
        b.append(a[i])

print(b)    '''

def fact(n):
    f=1
    if n==0 or n==1:
        return 1
    
    else:
        for i in range(1,n+1):
            f=f*i
        return f

def strong(n):
    sum=0
    temp=n
    while(n>0):
        dig=n%10
        sum+=fact(dig)
        n=n//10
    if(sum==temp):
        return True
    return False

s=146
print(strong(s))  # True
