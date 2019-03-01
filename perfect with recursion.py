def perfect_number(n,i):
    if n%i==0 and n!=i:
        return i
    else:
        return perfect_number(n,i)+perfect_number(n,i+1)

x=int(input())
perfect_number(x,1)
if perfect_number(x,1)==x:
    print("perfect number")

else:
    print("non perfect number")
