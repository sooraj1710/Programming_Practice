# n=int(input("n: "))
# arr=[]
# prime_arr=[]
# for i in range(1, n+1):
#     if n%i==0:
#         arr.append(i)

# print(arr)
# for i in range(1,len(arr)):
#     if arr[i]>1:
#         flag=0
#         for j in range(2,i//2 + 1):
#             if arr[i]%j==0:
#                 flag=1
#                 break
#             else:
#                 prime_arr.append(arr[i])
# print(prime_arr)
def is_prime(x):
    prime=0
    if x==1:
        prime=0
    elif x==0:
        prime=0
    elif x==2:
        prime=1
    else:
        for i in range(2,x):
            if x%i!=0:
                prime=1
                
            else:
                prime=0
                break
    if(prime==1):
        return True
    else:
        return False
n=int(input("n: "))
arr=[]
for i in range(1, n+1):
    if n%i==0:
        arr.append(i)

print(arr)

res=[]
for i in range(len(arr)):
    if is_prime(arr[i]):
        res.append(arr[i])
print(res)
