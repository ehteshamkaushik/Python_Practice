n=int(input())
m=int(input())
x=0
while 1:
    z=n%10
    if z==m:
        x=x+1
    n=n//10
    if n==0:
        break
print(x)
