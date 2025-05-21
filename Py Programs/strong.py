def fact(m):
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

a=int(input("Enter: "))
res=strong(a)
print(res)