def bubble_sort(a):
  for i in range(len(a)-1,0,-1):
    swapped=False
    for j in range(0,i+1):
      if a[j]>a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
        swapped=True
        #print(a)   #comment in this line to see a simulation of the bubble sort algorithm
    if not swapped:
      return
bubble_sort([9,1,3,-8,5,-11,1])
