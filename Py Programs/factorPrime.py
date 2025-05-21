def primefact(n):
    prime=[]
    d=2
    while d<=n:
        if n%d==0:
            prime.append(d)
            n=n/d
        else:
            d+=1
    return prime

print(primefact(18))