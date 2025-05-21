enter=[4,6,3,4,6]
leave=[1,3,5,2,7]

inside=[]
f=0
for i in range(0,len(enter)):
    f+=enter[i]-leave[i]
    inside.append(f)
    
print(max(inside))