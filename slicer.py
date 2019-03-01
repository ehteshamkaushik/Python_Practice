def slicer(src_str,start,end):
  res=""
  for i in range(start,end):
    res=res+src_str[i]
  return res

src_str=input()
start=int(input())
end=int(input())
print(slicer(src_str,start,end))
