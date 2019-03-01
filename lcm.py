n=int(input())
x=int(input())
for i in range(n-1):
    y=int(input())
    a=max(x,y)
    b=min(x,y)
    i=1
    while 1:
        if (a*i)%b==0:
            x=a*i
            break
        i=i+1
print('lcm is',x)
