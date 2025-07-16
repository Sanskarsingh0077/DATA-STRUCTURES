class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Top Down Memoized Solution
        nums.sort()
        n = len(nums)
        '''
        dp = [[-1]*(n+1) for _ in range(n+1)]

        def solve(index,prev):
            if index == n:
                return []

            if dp[index][prev] != -1:
                return dp[index][prev]

            not_take = solve(index+1,prev)
            
            take = []
            if nums[index] % nums[prev] == 0 or nums[prev] % nums[index] == 0 or prev == -1:
                take = [nums[index]] + solve(index+1,index)

            dp[index][prev] = take if len(take) > len(not_take) else not_take
            return dp[index][prev]

        
        return solve(0,-1)

        '''


        # Bottom Up

        
        dp = [[num] for num in nums]  # dp[i] stores the divisible subset ending at index i
        max_subset = []

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]

            if len(dp[i]) > len(max_subset):
                max_subset = dp[i]

        return max_subset


                