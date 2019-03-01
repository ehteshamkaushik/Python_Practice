a=int(input())
b=int(input())
c=int(input())
d=(b*b)-(4*a*c)
if d>=0:
    e=(-b+(b*b-4*a*c)**.5)/(2*a)
    f=(-b-(b*b-4*a*c)**.5)/(2*a)
    print("the roots are:",e,f)
else:
    print("IMAGINARY")
