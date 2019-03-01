n=int(input())
x=[]

for i in range(n):
    x.append(int(input()))

min=x[0]
for j in range (1,len(x)):
    if x[j]<min:
        min=x[j]

print(min)

