def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)


m=int(input())
n=int(input())
print(gcd(m,n))
