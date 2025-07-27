def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        
        i = 0
        j = 1

        n = len(nums)

        while j+1 < n:
            if (nums[i] < nums[j] and nums[j]> nums[j+1]) or (nums[i]> nums[j] and nums[j]<nums[j+1]):
                ans += 1
                i = j
            j += 1

        return ans