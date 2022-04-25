def insertionsort(arr):
    for i in range(1,len(arr)):
        val=arr[i]
        pos=i-1
        while pos>=0 and val<arr[pos]:
            arr[pos+1]=arr[pos]
            pos-=1
        arr[pos+1]=val
    print(arr)


insertionsort([9, -3, 5, 2, 6, 8, -6, 1, 3])