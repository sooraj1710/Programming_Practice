def linear(size, arr, search):
    for i in range(size):
        if arr[i]==search:
            return i
result=-1
size=int(input("enter the size of the array:"))
array= [0 for i in range(size)]
for i in range(size):
    array[i]=input("Enter the value")
search=input("Enter the search element")
result= linear(size, array, search)
if result!=-1:
    print("Found at index", result)
else:
    print("Not found")
