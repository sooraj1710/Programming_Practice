def BinarySearch(arr, low, high, key):
    if high>=low:
        mid=(high+low)//2
        if (arr[mid]==key):
            return mid
        elif (arr[mid]>key):
            return BinarySearch(arr,low, mid-1,key)
        else:
            return BinarySearch(arr, mid+1, high, key)
    else:
        return 1
l=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
    value=int(input("Enter the value"))
    l.append(value)
BinarySearch(l)
print("The sorted list is:",l)
            
