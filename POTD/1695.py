class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        # Sliding Window Classic 
        '''
        n = len(nums)
        i = 0
        j = 0
        set_nums = set()
        currsum = 0
        ans = 0

        while j < n:
            if nums[j] not in set_nums: # Increasing window Size
                currsum += nums[j]
                ans = max(currsum,ans)

                set_nums.add(nums[j])

                j += 1

            else: 
                # Shrinking Window
                while i < n and nums[j] in set_nums:
                    currsum -= nums[i]
                    set_nums.remove(nums[i])
                    i += 1

        return ans

        '''
        n = len(nums)

        array = [-1]* (10**4 + 1)
        i = 0
        curr = 0
        result = 0

        for j in range(n):
            if array[nums[j]] != -1 and array[nums[j]] >= i:
                # Element seen before and is inside current window
                # Shrink window
                while i <= array[nums[j]]:
                    curr -= nums[i]
                    i += 1

            curr += nums[j]
            result = max(result, curr)
            array[nums[j]] = j  # Update latest index

        return result