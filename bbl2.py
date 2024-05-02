a= [10,2,304,5,2,40,445]
for i in range (len(a)):
    for j in range(i+1,len(a)-1):
        if a[i]> a[j]:
            a[i],a[j]=a[j],a[i]

print(a)

import time
def bubble_sort(arr):
    n=len(arr)
    swapped =True
    while swapped:
        swapped=False
        if arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            swapped=True

            n-=1
arr=[66,77,87,99,5,3,4]
print("Original array:",arr)
Star_time=time.time()
bubble_sort(arr)
end_time=time.time()
print("Sorted array:",arr)
print("Execution:",end_time-Star_time,"seconds")

            