def fact(n):
    f=1
    if s==0 or s==1:
        return 1
    for i in range(1,n+1):
        f=i*f
    return f
s=int(input("Enter: "))
a=fact(s)
print(a)

