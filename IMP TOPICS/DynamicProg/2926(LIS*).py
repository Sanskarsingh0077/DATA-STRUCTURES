from sortedcontainers import SortedDict
class Solution:

    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        #Top Down Approach
        
        '''
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n+1)]

        def solve(index,prev):
            if index >= n:
                return 0

            if dp[index][prev+1] != -1:
                return dp[index][prev+1]

            take = 0
            if prev == -1 or nums[index] - index >= nums[prev] - prev:
                take = nums[index] + solve(index+1,index)

        
            skip = solve(index+1,prev)

            dp[index][prev+1] = max(take,skip)
            return dp[index][prev+1]

        if max(nums) <= 0:
            return max(nums)
        else:
            return solve(0,-1)

        '''

        # Botttom Up Approach
        '''
        t = [0] * (n)
        maxSum = 0

        if max(nums) <= 0:
            return max(nums)

        for i in range(n):
            t[i] = nums[i]

        for i in range(n):
            for j in range(i):
                if nums[i] - i >= nums[j] - j:
                    t[i]= max(t[i],t[j]+nums[i])
            maxSum = max(maxSum,t[i])

        return maxSum

        '''