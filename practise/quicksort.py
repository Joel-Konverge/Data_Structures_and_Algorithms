
def partition(arr,st,j):
    p=st
    i=st+1
    while j>i:
        while i<j and arr[i]<arr[p]:
            i+=1
        while j>0 and arr[j]>arr[p]:
            j-=1
        if j<i:
            break
        arr[i],arr[j]=arr[j],arr[i]
    if arr[p]>arr[j]:
        arr[p],arr[j]=arr[j],arr[p]
    return j



def quicksort(array, st, en):
    if st>=en:
        return
    par=partition(array,st,en)
    quicksort(array,st,par-1)
    quicksort(array,par+1,en)
    return array


arr=[9, -3, 5, 2, 6, 8, -6, 1, 3]
quicksort(arr,0,len(arr)-1)
print(quicksort(arr,0,len(arr)-1))