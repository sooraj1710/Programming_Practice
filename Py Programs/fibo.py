def fibo(n):
    if n<=1:
        return
    else:
        return (fibo(n-1)+fibo(n-2))
num=int(input("Fibonacci sequence upto:"))
if num<0:
    print("Enter positive number")
else:
    print("Fibonacci sequense:"))
    for i in range(num):
        print(fibo(i))
