x=int(input())
x=x*3.14/180
sum=x
a=x
for n in range(1,1000,2):
    z=-x*x/(2*n*(2*n+1))
    a=a*z
    sum=sum+a
print(sum)
    
