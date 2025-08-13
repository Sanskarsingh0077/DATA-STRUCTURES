def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def solve(rem):
            if rem == 0:
                return 1

            if rem < 0:
                return 0

            if rem in dp:
                return dp[rem]

            ways = 0
            for num in nums:
                ways += solve(rem - num)

            dp[rem] = ways
            return dp[rem]

        return solve(target)