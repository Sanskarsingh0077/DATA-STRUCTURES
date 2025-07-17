def maximumLength(self, nums: List[int], k: int) -> int:
        #Bottom Up

        n = len(nums)
        dp = [[1] * n for _ in range(k)]
        result =0
        
        for i in range(n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                
                dp[mod][i] = max(dp[mod][i], 1+ dp[mod][j])
                result = max(result, dp[mod][i])

        return result