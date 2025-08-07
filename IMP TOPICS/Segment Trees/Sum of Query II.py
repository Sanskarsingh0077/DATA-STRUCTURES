'''
C++ Solution 1104/1104 cases

class Solution {
  public:
    void buildsegmentTree(int idx, int left,int right, vector<int> &segmentTree, int arr[]){
        if(left == right){
            segmentTree[idx] = arr[left];
            return;
            
        }
        int mid = (left+right)/2;
        
        buildsegmentTree(2*idx+1,left,mid,segmentTree,arr);
        buildsegmentTree(2*idx+2,mid+1,right,segmentTree,arr);
        segmentTree[idx] = segmentTree[2*idx+1]+segmentTree[2*idx+2];
        
    }
    
    int querySegmentTree(int start, int end, int idx, int left, int right, vector<int>& segmentTree){
        if(left > end || right < start){
            return 0;
        }
        if(left>= start && right <= end){
            return segmentTree[idx];
            
        }
        else{
            int mid = (left+right)/2;
            return querySegmentTree(start, end, 2*idx+1, left, mid, segmentTree)+ querySegmentTree(start,end, 2*idx+2, mid+1,right,segmentTree);
        }
    }
  
  
    vector<int> querySum(int n, int arr[], int q, int queries[]) {
        // code here
        vector<int> segmentTree(4*n);
        buildsegmentTree(0,0,n-1,segmentTree,arr);
        
        vector<int> result;
        
        for(int i = 0; i < 2*q ; i += 2){
            int start = queries[i]-1;
            int end = queries[i+1]-1;
            
            result.push_back(querySegmentTree(start,end, 0,0,n-1, segmentTree));
            
        }
        return result;
    }
};
'''

# Python Solution 1050/1104 Passed Recursion TLE

class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        result = []
        segmentarr = [0]*(4*n)
        
        
        def buildtree(idx,left,right):
            
            
            if left == right:
                segmentarr[idx] = arr[left]
                return
            
            mid = (left+right)//2
            
            buildtree(2*idx+1,left,mid)
            buildtree(2*idx + 2, mid+1, right)
            segmentarr[idx] = segmentarr[2*idx+1]+segmentarr[2*idx+2]
            
        def Query(start, end, idx, left, right):
            if (left > end) or (right < start):
                return 0
                
            if left >= start and right <= end:
                return segmentarr[idx]
                
            else:
                mid = (left+right)//2
                return Query(start, end, 2*idx+1, left, mid) + Query(start,end, 2*idx+2,mid+1,right)
            
        buildtree(0, 0 , n-1)
        
        for i in range(0,2*q,2):
            start = queries[i]-1
            end = queries[i+1]-1
            
            result.append(Query(start,end, 0, 0, n-1))
            
        return result