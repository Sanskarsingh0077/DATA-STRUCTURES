class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # DP Knapsack Solution

        N = len(strs)

        count = [0]*N
        for i in range(N):
            zeroes = 0
            ones = 0

            for ch in strs[i]:
                if ch == '0':
                    zeroes += 1

                else:
                    ones += 1

            count[i] = (zeroes,ones)

        dp = [[[-1] * (n+1) for _ in range(m + 1)] for _ in range(N + 1)]

        def solve(idx, m, n):
            if idx >= N or (m == 0 and n == 0):
                return 0

            if dp[idx][m][n] != -1:
                return dp[idx][m][n]

            take = 0

            if count[idx][0]<= m and count[idx][1] <= n:
                take = 1 + solve(idx+1, m - count[idx][0] , n - count[idx][1])

            skip = solve(idx+1, m, n)

            dp[idx][m][n] = max(take, skip)

            return dp[idx][m][n]


        return solve(0,m,n)