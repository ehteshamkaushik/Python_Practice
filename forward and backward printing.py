#For practice
#Printing 1 to n-1 using for
 
#range(start,end,step)
def forward_Printing1(n):
    for i in range(1,n,2):
        print('Value of i =', i)
         
#range(start,end)--> by default step = 1
def forward_Printing2(n):
    for i in range(1,n): #[1 to n-1]
        print('Value of i =', i)
 
 
#range(end) --> by default start = 0 and step = 1
def forward_Printing3(n):
    for i in range(n): #[0 to n-1]
        print('Value of i =', i)
 
 
n = int(input())
 
print('************Forward Printing version 1**********')
forward_Printing1(n)
print('************Forward Printing version 2**********')
forward_Printing2(n)
print('************Forward Printing version 2**********')
forward_Printing3(n)
 
 
#For practice
#Printing n to 1 using for
#range(start,end,step)
def backward_Printing(n):
    for i in range(n,0,-1): #[n to 1]
        print('Value of i =', i)
         
 
# use range(n,-1,-1) to print [n to 0]
def backward_printing1(n):
    for i in range(n,-1,-1):
        print('value of i =',i)
print('************Backward Printing**********')
backward_Printing(n)
print('************Backward Printing1**********')
backward_printing1(n)
