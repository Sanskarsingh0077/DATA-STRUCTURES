def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()

        for i in range(n-1,1,-1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i] + nums[i-1] + nums[i-2]

        return 0