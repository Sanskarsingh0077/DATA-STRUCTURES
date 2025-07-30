def longestSubarray(self, nums: List[int]) -> int:
        maxAND = max(nums)
        max_len = 0
        curr_len = 0

        for i in nums:
            if i == maxAND:
                curr_len += 1
                max_len = max(max_len, curr_len)

            else:
                curr_len = 0

        return max_len