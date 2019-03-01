n=int(input())
a=[]
sum=0
for i in range(n):
    y=int(input())
    a.append(y)
    if y%2==0:
        sum=sum+y
print(sum)
        
