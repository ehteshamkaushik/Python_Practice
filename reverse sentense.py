def reverse_sentence(s):
  words=s.split()
  words.reverse()
  return " ".join(words)
    
s=input()
print(reverse_sentence(s))
