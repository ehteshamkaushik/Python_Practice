def lcm(a,b):
    x=max(a,b)
    y=min(a,b)
    i=1
    while 1:
        if (x*i)%y==0:
            lcm=x
            *i
            break
        i=i+1
    return lcm


n=int(input())
x=int(input())
for i in range(n-1):
    y=int(input())
    x=lcm(x,y)
print('lcm is',x)
