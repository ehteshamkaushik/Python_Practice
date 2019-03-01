def input_list(n):
  lst=[]
  while n>0:
    lst.append(int(input()))
    n-=1
    print(lst)
n=int(input())
print(input_list(n))
