def reverse_1(src_str):
  res=""
  for i in range(len(src_str)-1,-1,-1):
    res+=src_str[i]
  return res

def isPalindrome_1(src_str):
  return src_str==reverse_1(src_str)
src_str=input()
print(isPalindrome_1(src_str))
