def sum_list_1(a):
  _sum=0
  for num in a:
    _sum+=num
  return _sum


def consecutive_sum_1(a):
  ret=[]
  for i in range(len(a)):
    ret.append(sum_list_1(a[0:i+1]))
  print(a)
  return ret
a=[1,2,3,4,5]
print(consecutive_sum_1(a))
