def reverse_1(src_str):
  res=""
  for i in range(len(src_str)-1,-1,-1):
    res+=src_str[i]
  return res


src_str=input()
print(reverse_1(src_str))
