# Represent Segment Tree as an Array 

arr = [3, 1, 2, 7, 2, 1, 2, 3]
n = len(arr)
segmentarr = [0]*(4*n) # Segment Tree left = 2i + 1 and right = 2i+2

def buildTree(index,left,right):
    # Base Case
    if left == right:
        segmentarr[index] = arr[left]
        return
    
    
    mid = (left+right) // 2
    
    #Recursive Call
    buildTree(2*index+1,left,mid)
    buildTree(2*index+2 , mid+1, right)
    segmentarr[index] = segmentarr[2*index+1] + segmentarr[2*index+2]

    return segmentarr

buildTree(0, 0 , n-1)
print("Segment Tree:",segmentarr[:2*n])


# Range Sum Query For Segment Tree

def rangeSum(idx, start, end, left, right):
    # Out of left and right
    if (left > end) or (right < start):
        return 0
    
    # within left and right
    
    if left >= start and right <= end:
        return segmentarr[idx]
    
    # overlapping condition - some inside some outside
    
    else:
        mid = (left+right)//2
        ans = rangeSum(2*idx+1,start,end,left,mid) + rangeSum(2*idx+2,start,end,mid+1,right)
        return ans

ans = rangeSum(0,2,6,0,n-1)   
print("Range Sum:",ans)

# Time Complexity: O(Q*logn)
    
    
    
    