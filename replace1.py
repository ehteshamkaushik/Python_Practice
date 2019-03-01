def replace(s,q):
    for i in range(len(s)):
        flag=0
        for j in range(len(q)):
            if q[j]!=s[i+j]:
                flag=1
                break
        if flag==0:
            return i
    return -1
def replace1(s,q,d):
    
    index=replace(s,q)
    if index!=-1:
        st=""
        for i in range(index):
            st=st+s[i]
        st=st+d
        for j in range(index+len(q),len(s)):
            st=st+s[j]
        return st
    return s


s=input()
q=input()
d=input()
print(replace1(s,q,d))
