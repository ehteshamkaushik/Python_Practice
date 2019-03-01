def average(a):
    sum=0
    for i in range(len(a)):
        sum=sum+int(a[i])
    av=sum/2
    return av
def lst(n):
    a=[]
    for i in range(n):
        x=int(input())
        a.append(x)
    m=average(a)
    print(a)
    return m
n=int(input())
print(lst(n))
