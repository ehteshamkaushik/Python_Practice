def namta(n):
    for i in range(n,0,-1):
        for j in range(1,11,1):
            m=i*j
            print(i,'*',j,'=',m)

n=int(input())
namta(n)
