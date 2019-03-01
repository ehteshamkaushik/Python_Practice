def numcount(n,m):
    count=0
    while 1:
        if n%10==m:
            count=count+1
            n=n//10
            if n//10==0:
                break
    print(count)
            
m=int(input())
n=int(input())
numcount(m,n)

