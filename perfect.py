x=int(input())
sq=(x**.5)
sum=1
for i in range(2,int(sq+1)):
    if x%i==0:
        if sq==i:
            sum=sum+i
        else:
            sum=sum+i+x/i
if sum==x:
    print('Yes')
else:
    print('No')
