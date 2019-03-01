#nested iteration
 
def forward_Printing(n):
    for i in range(1,n): #[1 to n-1]
        print('********* i start *********')
        print('value of i = ', i)
        for j in range(1,n): #[1 to n-1]
                print('value of j =', j)
        print('********* i end *********')
 
 
n = int(input())
 
print('************ Forward Printing using nested for **********')
forward_Printing(n)
