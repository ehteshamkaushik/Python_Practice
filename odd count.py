def count_odd(a):
    cnt=0
    for i in range(len(a)):
        if int(a[i])%2!=0:
            cnt+=1
    return cnt
def lst(n):
    a=[]
    for i in range(n):
        x=int(input())
        a.append(x)
    res=count_odd(a)
    print(a)
    return res
n=int(input())
print(lst(n))
