n=int(input())
sum=0
tem=0
for i in range(n):
    x=int(input())
    if x>=0:
        sum=sum+1
    else:
        tem=max(tem,sum)
        sum=0
sum=max(tem,sum)
print(sum)
