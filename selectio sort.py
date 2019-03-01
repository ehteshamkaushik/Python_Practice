def selection_sort(a):
  for i in range(len(a)-1):
    min_index=i
    for j in range(i+1,len(a)):
      if a[j]<a[min_index]:
        min_index=j
      a[i],a[min_index]=a[min_index],a[i]
      print(a)   #comment in this line to see a simulation of the selection sort algorithm
selection_sort([9,7,2,-7,8,-2,13,1])
