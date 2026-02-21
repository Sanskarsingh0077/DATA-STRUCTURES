class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        res = []
        subset = []
        def decision(idx):
            
            if idx == len(nums):
                return res.append(subset.copy())

            # Backtracking
            subset.append(nums[idx]) #do
            decision(idx + 1) #explore
            subset.pop() #undo

            # Move Ahead Recursion
            decision(idx + 1)

        decision(0)
        return res
    
        '''
        
        res = []
        def backtrack(idx, path):
            res.append(path[:])
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
                
        backtrack(0, [])
        return res

