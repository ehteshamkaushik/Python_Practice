def in_fnc(src_str,qry_str):
    for i in range(0,len(src_str)-len(qry_str)+1):
        flag=0
        for j in range(len(qry_str)):
            if qry_str[j]!=src_str[i+j]:
                flag=1
                break
        if flag==0:
            return True

    return False
src_str=input()
qry_str=input()
print(in_fnc(src_str,qry_str))

    
