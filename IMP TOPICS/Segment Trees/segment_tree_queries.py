# Building the tree from segment_tree_build.py 

arr = [3,1,2,7]
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

# Update Segment Tree Query

def updateSegmentTree(indextoupdate, val, idx, left, right):
    if left == right:
        segmentarr[idx] = val
        return
    
    mid = (left + right)//2
    
    if indextoupdate <= mid:
        updateSegmentTree(indextoupdate, val, (2*idx)+1, left,mid)
    else:
        updateSegmentTree(indextoupdate, val, (2*idx)+2, mid+1, right)
    
    segmentarr[idx] = segmentarr[2*idx+1]+ segmentarr[2*idx+2]
    
updateSegmentTree(1,4,0,0,3)

print("Update Segment Tree:",segmentarr[:2*n])
    

# Time Complexity: O(logn) visiting only needed nodes.
