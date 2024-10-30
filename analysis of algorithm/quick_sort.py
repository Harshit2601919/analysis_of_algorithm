def quick_sort(arr,start,end):
    if start< end:
        new_pivot=partition(arr,start,end)
        quick_sort(arr,start,new_pivot-1)
        quick_sort(arr,new_pivot+1,end)

def partition(arr,start,end):
    pivot=arr[start]
    print(f"pivot is :{pivot}\t",end=" ")
    i=start+1
    for j in range(start+1,end+1):
        if arr[j]<pivot:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
        

    temp=arr[start]
    arr[start]=arr[i-1]
    arr[i-1]=temp
    print(f"array is {arr}")

    return i-1
                   
                    

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    array = []
    for i in range(0, n):
        temp = int(input(f"Enter the element {i + 1}: "))
        array.append(temp)

    print(f"before sorting : {array}")
    quick_sort(array,0,len(array)-1)
    print(array)


def quick_sort(arr,start,end):
    if start<end:
        new_pivot=partition(arr,start,end)
        quick_sort(arr,start,new_pivot-1)
        quick_sort(arr,new_pivot+1,end)


def partition(arr,start,end):
    pivot=arr[start]
    print(f"pivot is {pivot}",end=" ")
    i=start+1
    for j in range(start+1,end+1):
        if arr[j]<pivot:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1

        temp=arr[start]
        arr[start]=arr[i-1]
        arr[i-1]=temp
        print(f"array is {arr}")

    return i-1 
