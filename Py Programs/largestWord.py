s="hello my name is not lionelmessi"
word=s.split()
lenarr=[]
for i in word:
    lenarr.append(len(i))
print(lenarr)
maxx=max(lenarr)
i=lenarr.index(maxx)
print(word[i])