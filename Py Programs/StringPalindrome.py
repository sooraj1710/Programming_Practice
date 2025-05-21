def palin(s):
    temp=s
    i=0
    j=len(s)-1
    while(i<=j):
        if(temp[i]==temp[j]):
            flag=1
        else:
            flag=0
            break
        i=i+1
        j=j-1
    if(flag==1):
        return "Yes"
    else:
        return "No"
s="malayalam"
print(palin(s))  