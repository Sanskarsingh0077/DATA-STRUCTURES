class Solution:
    def fib(self, n: int) -> int:
        #DP Top- Down Memoization Approach:
        '''
        dp = [-1]*(n+1)

        def solve(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1

            if dp[n]!=-1:
                return dp[n]

            dp[n]=solve(n-1)+solve(n-2)
            return dp[n]
        
        return solve(n)
        '''
        #Bottom Up -- Tabulation(Optimal)

        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b