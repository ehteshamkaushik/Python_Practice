def ncr(n,r):
    if n==r or r==0:
        return 1
    else:
        return ncr(n-1,r)+ncr(n-1,r-1)





n=int(input())
r=int(input())
print(ncr(n,r))
