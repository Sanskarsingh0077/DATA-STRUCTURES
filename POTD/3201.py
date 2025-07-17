class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        countEven = 0
        countOdd = 0
        

        for num in nums:
            if num %2 == 0:
                countEven += 1

            else:
                countOdd += 1

        parity = nums[0]%2
        alternating = 1

        for i in range(n):
            currParity = nums[i] % 2

            if currParity != parity:
                alternating += 1
                parity = currParity


        return max(countEven, countOdd, alternating)
    
    '''
        #Top Down 
        def LIS(idx, prev, mod):
            if idx == len(nums):
                return 0  # since we count from 0 when no element picked

            take = 0
            if prev == -1 or (nums[prev] + nums[idx]) % 2 == mod:
                take = 1 + LIS(idx + 1, idx, mod)

            skip = LIS(idx + 1, prev, mod)

            return max(take, skip)

        return max(LIS(0, -1, 0), LIS(0, -1, 1))


        # Bottom UP
        n = len(nums)
        dp1 = [1]*n
        dp2 = [1]*n
        result =0
        
        for i in range(n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % 2
                if mod == 1:

                    dp1[i] = max(dp1[i],dp1[j]+1)
                    result = max(dp1[i],result)

                else:
                    dp2[i] = max(dp2[i],dp2[j]+1)
                    result = max(dp2[i],result)

        return result
    '''