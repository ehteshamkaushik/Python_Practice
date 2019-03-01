def prime_number(n):
    sq=int(n**.5)
    flag=1
    for j in range (2,sq+1,1):
        if n%j==0:
            flag=0
            break
    if flag==1:
        print(n)
 


n=int(input())
for i in range(2,n+1,1):
    prime_number(i)
