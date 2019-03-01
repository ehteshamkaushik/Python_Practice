n=int(input())
m=int(input())
count=0
while 1:
    if n%10==m:
        count=count+1
    n=n//10
print(count)
