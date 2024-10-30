arr=list(map(int,input("enter the elemets").strip().split()))
print("original array",arr)

for i in range(1,len(arr)):
    value=arr[i]
    j=i-1
    while j>=0 and value<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=value
    print("after pass",i,":",*arr)
print("sorted array",*arr)
    




arr=list(map(int,input("enter the elements").strip().split()))
print("original array",arr)

for i in range(1,len(arr)):
    value=arr[i]

    j=i-1
    while j>=0 and value<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=value
    print(f"after pass ",i,":",*arr)
print("sorted array",*arr)



arr=list(map(int,input("enter the elmenets").strip().split()))
print("original array is",arr)

for i in range(1,len(arr)):
    value=arr[i]
    j=i-1
    while j>=0 and value<arr[j]:
        arr[j+1]=arr[j]
        j-=1

    arr[j+1]=value
    print("after pass",i,":",*arr)

print("sorted array is ",*arr)    