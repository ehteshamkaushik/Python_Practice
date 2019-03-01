def gcd(a,b):
    x=max(a,b)
    y=min(a,b)

    if a%b==0:
        gcd=b
    else:
        while 1:
            t=a
            a=b
            b=t%b
            if a%b==0:
                gcd=b
                break
    return gcd



n=int(input())
x=int(input())
for i in range(n-1):
    y=int(input())
    x=gcd(x,y)
print("gcd is",x)
