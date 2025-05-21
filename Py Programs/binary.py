def binary(size, l ,search):
    low=1
    high=size
    while low<=high:
        mid=(low+high)//2
        if l[mid]==search:
            return mid
        elif l[mid]>search:
            low=1
            high=mid-1
        else:
            low=mid+1
            high=size

size=int(input("Enter the size"))
result=-1
l=[]
for i in range (size):
    value=(input("Enter the values"))
    l.append(value)
L=sorted(l)
search=(input("Enter the search element"))
result= binary(size, L ,search)
if result!=-1:
    print("The element found ",result)
else:
    print("Not found")
