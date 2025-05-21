'''s="aaabbccz"
m=list(s)
c=[0]*27
for i in range(len(m)):
    if m[i]!=' ':
        c[ord(m[i])-96]+=1
n=c.index(max(c))
# max=0
# for i in range(len(c)):
#     if(c[i]>max):
#         max=c[i]
#         ind=i
# print(ind)

print(chr(96+n))'''
s="aaabbcccd"
c=[0]*27
n=len(s)
res=[]
for i in range(n):
    c[ord(s[i]) - ord('a')]+=1
print(c)
for i in range(26):
    if c[i]>0:
        print(chr(i+97),"",c[i])
        res.append(chr(i+97))
        res.append(c[i])
for i in res:
    print(i,end="")