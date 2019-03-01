def count(src_str,qry_char):
  cnt=0
  for i in src_str:
    if i==qry_char:
      cnt+=1
  return cnt

src_str=input()
qry_char=input()
print(count(src_str,qry_char))
