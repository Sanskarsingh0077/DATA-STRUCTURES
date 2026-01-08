def findpeak(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = left + (right - left)// 2
        
        if arr[mid] < arr[mid+1]: # Shrink Right
            left = mid + 1
            
        elif arr[mid] > arr[mid+1]: # Shrink left
            right = mid
            
        else:
            right -= 1 # remove Duplicate elements
            
    return arr[left]


print(findpeak([1,2, 4, 8,8,9,6,5,4,3,2,1]))