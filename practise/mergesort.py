def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        arr1=arr[:mid]
        arr2=arr[mid:]
        merge_sort(arr1)
        merge_sort(arr2)
        i,j=len(arr1),len(arr2)
        a,b,c=0,0,0
        while a<i and b<j:
            if arr1[a]<arr2[b]:
                arr[c]=arr1[a]
                a+=1
            else:
                arr[c]=arr2[b]
                b+=1
            c+=1
        while a<i:
            arr[c]=arr1[a]
            a+=1
            c+=1
        while b<j:
            arr[c]=arr2[b]
            b+=1
            c+=1
        return arr   
        
        

print(merge_sort([8, 7, 6, 15, 3, 11]))
