class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False

            return True


        count = 0

        while not is_sorted(nums):
            index = 0
            min_sum = float('inf')
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    index = i

            
            nums[index] = min_sum
            nums.pop(index+1)

            count += 1

        return count
            