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
def remove_first_2(src_str,qry_str):
  index=find_2(src_str,qry_str)
  if index!=-1:
    res=""
    for i in range(index):
      res=res+src_str[i]
    for i in range(index+len(qry_str),len(src_str)):
      res=res+src_str[i]
    return res
  return src_str
src_str=input()
qry_str=input()
print(remove_first_2(src_str,qry_str))
