def isPrime(n):
  if n==1:
    return False      #1 is not prime by convention
  if n==2:
    return True       #2 is a prime
  for i in range(2,n):
    if n%i==0:
      return False
  return True



def print_prime(n):
  for i in range(1,n+1):
    if isPrime(i)==True:
      print(i)
 


n=int(input())
print_prime(n)
