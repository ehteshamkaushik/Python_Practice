def sum_list_1(a):
  _sum=0
  for num in range(len(a)):
    _sum=_sum+int(a[num])
  return _sum
a=list(input())
print(sum_list_1(a))
