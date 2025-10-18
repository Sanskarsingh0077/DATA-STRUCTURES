class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Take the smallest possible for the first element
        prev = nums[0] - k  
        count = 1  

        for i in range(1, n):
            minval = nums[i] - k
            maxval = nums[i] + k

            if prev < minval:
                prev = minval
            elif prev < maxval:
                prev += 1
            else:
                continue

            count += 1

        return count