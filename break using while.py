#break practice using while
#Printing 1 to n using while
 
def forward_Printing(n):
    i = 1; 
    while True:
        print('Value of i =', i)
        if(i == n):
            break
        i = i + 1
             
 
 
n = int(input())
 
print('************Forward Printing using While with break statement**********')
forward_Printing(n)
 
 
#break practice using while
#Printing n to 1 using while
def backward_Printing(n):
    i = n
    while True: #[n to 1]
        print('Value of i =', i)
        if i == 1:
            break
        i = i - 1
         
         
print('************Backward Printing using While with break statement**********')
backward_Printing(n)
