def input_list(n):
    lst=[]
    for i in range(n):
        x=int(input())
        lst.append(x)
    return lst

n=int(input())
lst1=input_list(n)
print(lst1)
n=int(input())
lst2=input_list(n)
print(lst2)

def sort_2_list(lst1,lst2):
     i=0
     j=0
     fl=[]
     while 1:
         if lst1[i]<lst2[j]:
             print('i is',i)
             fl.append(lst1[i])
             i=i+1
             print('f i is',i)
             print('lf is',fl)
             if i==len(lst1)+1:
                 break
         else:
             fl.append(lst2[j])
             print('j is',j)
             j=j+1
             print('f j is',j)
             print('fl is',fl)
             if j==len(lst2)+1:
                 break
     return fl

print(sort_2_list(lst1,lst2))
