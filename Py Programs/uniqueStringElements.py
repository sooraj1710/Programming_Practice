s="hello"
arr=[]
for i in range(len(s)):
    arr.append(s[i])
arrr=[]
for i in arr:
    if i not in arrr:
        arrr.append(i)

strr=""
for i in arrr:
    strr+=i

print(strr)