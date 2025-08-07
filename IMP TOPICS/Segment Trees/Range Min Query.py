# GFG Range Minimum Query

def constructST(arr, n):
    segmentTree = [0]*(4*n)
    
    def buildsegmentTree(idx, l, r, segmentTree, arr):
        if l == r:
            segmentTree[idx] = arr[l]
            return
            
        mid = (l+r)//2
        
        buildsegmentTree(2*idx+1,l,mid,segmentTree,arr)
        buildsegmentTree(2*idx+2,mid+1,r,segmentTree,arr)
        segmentTree[idx] = min(segmentTree[2*idx+1],segmentTree[2*idx+2])
    
    buildsegmentTree(0,0,n-1,segmentTree,arr)

    return segmentTree

#Search min element
def RMQ(st, n, qs, qe):
    def query(start, end, i, l, r, segmentTree):
        if l > end or r < start:
            return float('inf')
            
        if l >= start and r <= end:
            return segmentTree[i]
            
        else:
            mid = (l+r)//2
            return min(query(start,end,2*i+1,l,mid,segmentTree),query(start,end,2*i+2,mid+1,r,segmentTree))

    return query(qs,qe,0,0,n-1,st)