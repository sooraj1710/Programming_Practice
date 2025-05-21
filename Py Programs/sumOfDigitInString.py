s=input()
'''sum=sum(int(ch)for ch in s if ch.isdigit())
print(sum)'''
arr=[]
summ=0
for i in range(len(s)):
    if(s[i].isdigit()):
        arr.append(s[i])
print(arr)
for i in range(len(arr)):
    num=int(arr[i])
    summ+=num
print(summ)