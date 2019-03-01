def binary(n):
    sum =0
    while n>0:
         sum = sum + n%2
         n = n//2
    return sum



#main
n = int(input())
ans =0
for i in range(1,n+1,1):
    ans = ans + binary(i)

print(ans)
