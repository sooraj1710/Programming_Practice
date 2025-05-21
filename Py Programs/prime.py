'''def isprime(n):
    flag=0 
    if n==1:
        return True
    
    elif n==0:
        return False
    
    else:
        for i in range(2,n//2 +1):
            if(n%i!=0):
                flag=1
            else:
                flag=0
                break
        if (flag==1):
            return True
        else:
            return False
        
s=2
res=isprime(s)
print(res)'''
def isprime(n):
    flag=0
    if(n==0 or n==1):
        flag=0
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                flag=0
                break
            else:
                flag=1
    if flag==0:
        return False
    else:
        return True
    
res=isprime(11)
print(res)
