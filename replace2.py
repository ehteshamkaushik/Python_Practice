def replace2(s,q,d):
    for i in range(len(s)):
        if s[i:len(q)+i-1]==q:
            print(d,end='')
        else:
            print(s[i],end='')
s=input()
q=input()
d=input()
replace2(s,q,d)

            
