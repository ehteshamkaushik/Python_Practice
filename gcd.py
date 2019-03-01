
n=int(input())
z=int(input())
for i in range(n-1):
    y=int(input())
    b=min(y,z)
    a=max(y,z)
    if a%b==0:
        z=b
    else:
        while 1 :
            T=a
            a=b
            b=T%b
            if a%b==0:
                z=b   
                break    
       
print('gcd=',z)
