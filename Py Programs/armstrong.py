def amstrong(n):
    sum=0
    temp=n
    while(n>0):
        dig=n%10
        sum+=dig**3
        n//=10
    if(temp==sum):
        return True
    return False

a=int(input("Enter: "))
res=amstrong(a)
print(res)