def sum_list(n):
    a=[]
    _sum=0
    for i in range(n):
        x=input()
        a.append(x)
        _sum=_sum+int(a[i])
    print(a)
    return _sum
n=int(input())
print(sum_list(n))

