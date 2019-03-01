def bubble_sort(a):
  for i in range(len(a)-2,-1,-1):
    swapped=False
    for j in range(0,i+1):
      if a[j]>a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
        swapped=True
        print(a)   #comment in this line to see a simulation of the bubble sort algorithm
    if not swapped:
      return a
print(bubble_sort([9,7,2,-7,8,-2,13,1]))
