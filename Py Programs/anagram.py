def anagram(s,m):
    temp=s
    arr1=[]
    arr2=[]
    for i in range(len(s)):
        arr1.append(s[i])
    
    for i in range(len(m)):
        arr2.append(m[i])

    arr1.sort()
    arr2.sort()
    if(arr1==arr2):
        return True
    else:
        return False

s=anagram("cat","act")

print(s)