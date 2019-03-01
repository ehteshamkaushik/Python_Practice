def find_2(src_str,qry_str):
  for i in range(0,len(src_str)-len(qry_str)+1):
    flag=True
    for j in range(len(qry_str)):
      if qry_str[j]!=src_str[i+j]:
        flag=False
        break
    if flag==True:
      return i
  return -1
src_str=input()
qry_str=input()
print(find_2(src_str,qry_str))
