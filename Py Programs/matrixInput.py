n=8
res=[]
d=2
while d<=n:
    if n%d==0:
        res.append(d)
        n=n/d
    else:
        d=d+1
print(res)
