x=str(input())
y=str(input())
z=str(input())
n=len(x)

for i in range(0,n):
    if x[i]!=y:
        print(x[i],end="")
    else:
        print(z,end="")
