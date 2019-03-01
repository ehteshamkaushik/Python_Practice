def prime_n(n,i):
    if n==2:
        return True
    if n%i==0 and n!=2:
        return False
    elif i*i>n:
        return True
    else:
        return prime_n(n,i+1)



n=int(input())
i=2
count=0
j=2
#for j in range(2,n+1,1):
    #print(j,prime_n(j,i))
while 1:
    if prime_n(j,i)==True:
        count=count+1
    if count==n:
        print(j)
        break
    j=j+1
