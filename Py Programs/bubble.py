def bubbleSort(l):
    n = len(l)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j] > l[j + 1] :
                l[j], l[j + 1] = l[j + 1], l[j]
 
l = []
num=int(input("Enter the number of elements"))
for i in range(num):
    value=int(input("Enter the values"))
    l.append(value)
 
bubbleSort(l)
 
print ("Sorted array is:")
for i in range(len(l)):
    print (l[i])
