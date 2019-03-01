def maxn(n):
    x=n%10
    if n==0:
        return 0
    else:
        return max(x,maxn(n//10))



n=int(input())
print(maxn(n))
