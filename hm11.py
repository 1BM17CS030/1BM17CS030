a=0
b=1
n=int(input("enter a number"))
fib=[a,b]
while b<n:
 a,b=b,a+b
 fib.append(b)
print(fib)
