s="HellO SoOraJ"
up=[]
low=[]
for i in range(len(s)):
    if(s[i]!=' '):
        if s[i].isupper():
            up.append(s[i])
        else:
            low.append(s[i])
print(up)
print(low)

up_count=[0]*27
low_count=[0]*27

for i in range(len(up)):
    up_count[ord(up[i])-ord('A')]+=1
for i in range(len(low)):
    low_count[ord(low[i])-ord('a')]+=1
print(up_count)
print(low_count)

for i in range(len(up_count)):
    if up_count[i]>0:
        print(chr(i+ord('A'))," ",up_count[i])

for i in range(len(low_count)):
    if low_count[i]>0:
        print(chr(i+ord('a'))," ",up_count[i])