x=input()
y=input()
z=input()

for i in range(0,len(x)):
    if x[i]==y:
        p=i
        break
for j in range(p+1,len(x)-p+1):
    if x[j]==z:
        q=j
        break
for j in range(q,p,-1):
    print(x[j])
