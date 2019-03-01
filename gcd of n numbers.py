def gcd(m,n):
    if n==0:
        return m
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)


o=int(input())
m=int(input())
n=int(input())
cur=gcd(m,n)
for i in range(1,o-1,1):
    r=int(input())
print(gcd(r,cur))
