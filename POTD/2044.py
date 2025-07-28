def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0

        for num in nums:
            maxOR |= num

        currOR = 0

        dp = [[-1] * (maxOR+1) for _ in range(len(nums) + 1)]

        def countsubsets(idx , currOR, array, maxOR):
            
            if idx == len(nums):
                if currOR == maxOR:
                    return 1
                else:
                    return 0

            if dp[idx][currOR] != -1:
                return dp[idx][currOR]


            take = countsubsets(idx+1, currOR | nums[idx], nums, maxOR)
            skip = countsubsets(idx+ 1, currOR, nums, maxOR)

            dp[idx][currOR] = take + skip

            return dp[idx][currOR]

        
        return countsubsets(0, currOR, nums, maxOR)