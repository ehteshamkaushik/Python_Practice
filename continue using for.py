#continue practice using while
#Printing 1 to n using while: Only Even numbers
 
def forward_Printing(n):
    for i in range(1,n+1):
        if i%2 == 1:
            continue
        print('Value of i =', i)
       
             
 
 
n = int(input())
 
print('************Forward Printing using for with continue statement**********')
forward_Printing(n)
 
 
#continue practice using while
#Printing n to 1 using while: Only odd numbers
def backward_Printing(n):
    for i in range(n,0,-1): #[n to 1]
        if i%2 == 0:
            continue
        print('Value of i =', i)
         
         
         
print('************Backward Printing using for with continue statement**********')
backward_Printing(n)
