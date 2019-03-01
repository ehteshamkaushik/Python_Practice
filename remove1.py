def find_1(src_str,qry_str):
  for i in range(0,len(src_str)-len(qry_str)+1):
    if qry_str==src_str[i:i+len(qry_str)]:
      return i
  return -1


def remove_first_1(src_str,qry_str):
  index=find_1(src_str,qry_str)
  if index!=-1:
    return src_str[:index]+src_str[index+len(qry_str):]
  return src_str


src_str=input()
qry_str=input()
print(remove_first_1(src_str,qry_str))
