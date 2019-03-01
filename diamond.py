def diamond(n):
    #upper triangle
    for i in range(1,n+1,1):

        #space print
        for j in range(1,2*(n-i)+1,1):
            print(end=" ")
        #number print
        for j in range(1,2*i,1):
            print(j,end=" ")

        #newline
        print()

    #lower triangle
    for i in range(1,n,1):

        #space print
        for j in range(1,2*i+1,1):
            print(end=" ")
        #number print
        for j in range(1,2*(n-i),1):
            print(j,end=" ")

        #newline
        print()



#main
n = int(input())
diamond(n)
