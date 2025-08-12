def numberOfWays(self, n: int, x: int) -> int:
        dp = [[-1]*(n+1) for _ in range(n+1)]
        m = 10**9+7
        
        def solve(rem,num):

            if rem == 0:
                return 1

            if n < 0:
                return 0

            if num**x > rem:
                return 0

            if dp[rem][num] != -1:
                return dp[rem][num]


            take = solve(rem-num**x, num+1)
            not_take = solve(rem, num+1)

            dp[rem][num] = (take+ not_take)%m
            return dp[rem][num]

        
        return solve(n,1)