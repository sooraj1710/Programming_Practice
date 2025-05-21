def asc(n):
    h=ord(n)
    return h

ch="hello"
arr=[]
for i in range(len(ch)):
    arr.append(ch[i])
res=[]
for i in range(len(arr)):
    res.append(asc(arr[i]))
print(res)
