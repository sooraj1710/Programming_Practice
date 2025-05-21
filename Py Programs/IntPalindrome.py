def palin(n):
    temp=n
    ans=0
    while(temp>0):
        dig=temp%10
        ans=ans*10+dig
        temp=temp//10
    if(n==ans):
        return True
    else:
        return False
    
ns=int(input("enter: "))
print(palin(ns))