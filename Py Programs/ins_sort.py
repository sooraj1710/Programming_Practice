def insertion_sort(l):
    for i in range(1,len(l)):
        element=l[i]
        j=i-1
        while(j>=0) and (element<l[j]):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=element
    return l
l=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
    value=int(input("Enter the value"))
    l.append(value)
insertion_sort(l)
print("The sorted list is:",l)
            
