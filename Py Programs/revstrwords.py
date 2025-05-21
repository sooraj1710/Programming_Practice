s="hello jaroos"
n=list(s)
print(ord('a'))
m=[0]*27
for i in range(len(n)):
    if n[i]!=' ':
        m[ord(s[i])-96]+=1

for i in range(len(m)):
    if m[i]!=0:
        print(str(m[i])+ (chr(i+96)), end="")

# a=[1,2,6,3,5,1,2,1,1,3,2,5]
# m=[0]*(max(a)+1)
# for i in range(len(a)):
#     m[a[i]]+=1


    