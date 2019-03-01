def it(i):
    if i==1:
        return 1
    else:
        return i*i+it(i-1)

def series(n):
    if n==1:
        return 1
    else:
        return it(n)+series(n-1)




n=int(input())
print(series(n))
