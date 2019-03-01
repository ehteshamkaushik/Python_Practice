n=int(input())
x=n*3.14/180
sum=x
a=x
for p in range(1,1000,2):
    z=-(x*x)/(2*p*(2*p+1))
    a=a*z
    sum=sum+a
print(sum)
