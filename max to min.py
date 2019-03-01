a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
    if b>c:
        print('a>b>c',a,b,c)
    else:
        print('a>c>b',a,c,b)
if b>a and b>c:
    if a>c:
        print('b>a>c',b,a,c)
    else:
        print('b>c>a',b,c,a)
if c>a and c>b:
    if a>b:
        print('c>a>b',c,a,b)
    else:
        print('c>b>a',c,b,a)
