def input_list(n):
  lst=[]
  while n>0:
    lst.append(int(input()))
    n-=1
  return lst

def input_2D_list(n,m):
  lst=[]
  while n>0:
    lst.append(input_list(m))
    n-=1
  return lst
n=int(input())
m=int(input())
print(input_2D_list(n,m))
