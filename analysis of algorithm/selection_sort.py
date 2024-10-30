arr=list(map(int,input("enter the elemets").strip().split()))
print("original array",arr)

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j
    
    arr[i],arr[min_idx]=arr[min_idx],arr[i]
    print("after",i+1,"pass",*arr)

print("sorted ",*arr)



arr=list(map(int,input("enter the elements").strip().split()))
print("original array",arr)

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:

         min_idx=j

    arr[i],arr[min_idx]=arr[min_idx],arr[i]
    print("after pass",i+1,":",*arr)

print("sprted array is ",*arr)




arr=list(map(int,input("enter the elemenst").strip().split()))
print("original arr",arr)

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
         min_idx=j
    
    arr[i],arr[min_idx]=arr[min_idx],arr[i]
    print("after pass",i+1,":",*arr)

print("original array",*arr)