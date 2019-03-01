n=int(input())
for i in range(2,n+1,1):
    sq=int(i**.5)
    flag=0
    for j in range(2,sq+1,1):
        if i%j==0:
            flag=1
    if flag==0:
        print(i)
