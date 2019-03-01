def rec_prime(n,i):
    if n<=i:
        return True
    if n%i==0:
        return False
    else:
        return rec_prime(n,i+1)

n=int(input())
print(rec_prime(n,2))
