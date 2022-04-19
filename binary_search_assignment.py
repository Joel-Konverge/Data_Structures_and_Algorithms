#using Lineat Search

def count_rotations(nums):
    #run the loop till the length of nums-1 to avoid index out of range error as we are comparing it with i+1
    for i in range(len(nums)-1):
        #return the number of rotation by checking if the i+1 element is smaller than i 
        if nums[i]>nums[i+1]:
            return i+1
    return 0


print(count_rotations([1, 2, 3, 4, 5, -1, 0]))

#Using Binary Search

def count_rotations(nums):
    l=0
    h=len(nums)-1
    while l<=h:
        mid=(l+h)//2
        #check if the number in the middle is less than the previous element
        if nums[mid]<nums[mid-1]:
            return mid
        #if the middle number is smaller than the last element then the answer lies on the left side
        elif nums[mid]<nums[h]:
            h=mid-1
        #if the middle number is greater than the last element then the answer lies on the right side
        else:
            l=mid+1        
    #in case if none of the above conditions are satisfied   
    return 0

print(count_rotations([4,5,6,7,8,1,2,3]))