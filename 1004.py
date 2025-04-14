class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=0

        zeroes_count =0
        max_ones= 0 

        n=len(nums)

        for end in range(n):
            if nums[end] == 0:
                zeroes_count +=1
            
            while zeroes_count> k:
                if nums[start] == 0:
                    zeroes_count-=1
                
                start+=1

            max_ones = max(max_ones,end+1-start)

        return max_ones
    

      '''
         Logic :
# Sliding window approach:
# - Move 'end' to expand the window
# - Count how many 0s are in the current window
# - If 0s exceed k, shrink the window from the left by moving 'start'
# - Keep updating the max window size where 0s ≤ k

# Goal: Max consecutive 1s by flipping at most k zeroes
# Keep window valid → at most k zeroes inside

     '''