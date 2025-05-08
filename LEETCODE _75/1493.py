class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Approach:
        # Approach:
        # - Use sliding window to track the longest subarray with at most one 0
        # - Expand the window by moving the right pointer (j)
        # - If more than one 0 is in the window, shrink it from the left (move i)
        # - Keep updating the maximum length of the valid window
        '''
        
        i=0
        j=0
        zeroCount=0
        result=0

        n=len(nums)

        for j in range(n):
            if nums[j]==0:
                zeroCount+=1

            while zeroCount > 1:
                if nums[i]==0:
                    zeroCount-=1
                i+=1

            result=max(result, j-i)

        return result
    

    '''
    class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
    
    
        #Approach 2(i ko last zero ke next pr bulaao)
        # Approach:
        # - Use two pointers (i and j) to create a window
        # - Track the index of the last seen 0 (since we can only delete one 0)
        # - When a new 0 is found, move the start of the window (i) to one after the previous 0
        # - Update the result with the size of the current valid window (j - i)

        i = 0
        j= 0
        last_zero_index=-1#(since cant use 0 index)

        result= 0

        while j < len(nums):
            if nums[j] == 0:
                i = last_zero_index +1
                last_zero_index = j
            
            result = max(result,j-i)
            j+=1
        
        return result
    '''