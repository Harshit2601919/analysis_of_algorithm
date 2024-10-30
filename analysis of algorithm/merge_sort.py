def merge_sort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, low, mid, high)

    return A

def merge(A, low, mid, high):
    i = low
    j = mid + 1
    k = low
    B = [0] * (high + 1)

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1
    while j <= high:
    
        B[k] = A[j]
        j += 1
        k += 1

    for k in range(low, high + 1):
        A[k] = B[k]

    print(f"After merge: {A}\n")

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    array = []
    for i in range(0, n):
        temp = int(input(f"Enter the element {i + 1}: "))
        array.append(temp)

    print("Original array:", array)
    array = merge_sort(array, 0, n - 1)
    
    print("Sorted array:", array)


def merge(A,low,high):
    if low<high:
        mid=(low+high)//2
        merge(A,low,mid)
        merge(A,mid+1,high)
        merge_sort(A,low,mid,high)

    return A

def merge_sort(A,low,mid,high):
    i=low
    j=mid+1
    k=low
    B=[0]*(high+1)

    while i<=mid and j<=high:
        if A[i]<=A[j]:
            B[k]=A[i]
            i+=1

        else:
            B[k]=A[j]
            j+=1
        k+=1

    while i<=mid:
        B[k]=A[i]
        i+=1
        k+=1

    while j<=high:
        B[k]=A[j]
        j+=1
        k+=1

    for k in range(low,high):
        A[k]=B[k]

    print(f"after merge {A}\n")



if __name__=="__main__":
    n=int(input("enter the number of elemenst"))
    array=[]
    for  i in range(0,n):
      temp=int(input(f"enter the elemenst {i+1}"))
      array.append(temp)

    arr=merge(array,0,n-1)
    print(f"sorted array",arr)