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