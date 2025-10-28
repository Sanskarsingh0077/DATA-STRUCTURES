class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Brute Force Simulation
        '''
        n = len(nums)
        result = 0
        count = 0 #count of non zero

        def check(nums, count, idx, dxn):
            nums = nums[:]
            while 0 <= idx < n and count > 0:
                if nums[idx] > 0:
                    nums[idx] -= 1
                    dxn *= -1
                    if nums[idx] == 0:
                        count -= 1

                idx += dxn

            return count == 0

        for i in range(n):
            if nums[i] != 0:
                count += 1

        for i in range(n):
            if nums[i] == 0:
                if check(nums, count, i , -1):
                    result += 1

                if check(nums, count, i, 1):
                    result += 1

        return result

        '''

        # Optimal Solution

        total = sum(nums)
        curr = 0
        res = 0

        for i in range(len(nums)):
            curr += nums[i]
            left = curr
            right = total - left

            if nums[i] != 0:
                continue

            if left == right:
                res += 2

            if abs(left-right)== 1:
                res += 1

        return res

