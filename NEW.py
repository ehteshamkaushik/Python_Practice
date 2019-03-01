num=float(input())
if num>100:
    print("INVALID")
elif 80<=num<100:
    print("A+")
elif 70<=num<80:
    print("A")
elif 60<=num<70:
    print("A-")
elif 50<=num<60:
    print("B")
elif 40<=num<50:
    print("C")
elif 33<=num<40:
    print("D")
elif num<0:
    print("INVALID")
else:
    print("F")
