n=int(input())
for i in range(2,n+1,1):
    sq=int(i**.5)
    com=1
    for j in range(2,sq+1):
        if i%j==0:
            com=0
            
    if com==1:
        print(i)
            



