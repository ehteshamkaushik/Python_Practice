def lst_input(n):
    a=[]
    for i in range(n):
        a.append(int(input))
        print(a)


def sum_list_1(a):
  _sum=0
  size=len(lst_input(n))
  for num in range(size):
    _sum=_sum+a[num]
  return _sum

n=int(input())
print(sum_list_1(a))
