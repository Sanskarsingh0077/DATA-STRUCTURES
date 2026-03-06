class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]

        curr_min = curr_max = 0

        for i in range(len(nums)):
            curr_max = max(nums[i], curr_max+nums[i])
            max_sum = max(max_sum, curr_max)

            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(curr_min, min_sum)

        if max_sum < 0:
            return max_sum

        total = sum(nums)
        
        return max(max_sum, total - min_sum)