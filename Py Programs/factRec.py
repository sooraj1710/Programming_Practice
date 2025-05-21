def fact(n):
    f=1
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Eneter: "))
res=fact(n)
print(res)