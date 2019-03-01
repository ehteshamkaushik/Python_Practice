n=int(input())
for i in range(2,n+1,1):
    sq=int(i**0.5)
    flag=1
    for j in range(2,sq+1,1):
        if i%j==0:
            flag=0
    if flag==1:
        print(i)
