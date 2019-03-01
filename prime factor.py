def prime_factorization(n):
  div=2
  while n>1:
    cnt=0
    while n%div==0:
      cnt=cnt+1
      n=n//div
    if cnt>0:
      print(div,"^",cnt,end=" ",sep="")
      if n!=1:
        print("*",end=" ")
    div=div+1
  print()
  return


n=int(input())
prime_factorization(n)
