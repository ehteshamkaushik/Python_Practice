def range_reverse(src_str,start,end):
    s=src_str[end:start:-1]
    print(s)
    o=src_str[:start+1]
    print(o)
    p=src_str[end+1:]
    print(p)

    
src_str=input()
start=int(input())
end=int(input())
range_reverse(src_str,start,end)
