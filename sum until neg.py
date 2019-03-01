def sum_until_neg(a):
  _sum=0
  for i in range(len(a)-1):
    print('i is',a[i])
    if a[i]<0:
      break
    else:
      _sum=_sum+a[i]
      print('_sum is',_sum)
  return _sum
def input_list(n):
  a=[]
  for i in range(n):
    x=int(input())
    a.append(x)
  res=sum_until_neg(a)
  print(a)
  return res

n=int(input())
print(input_list(n))
