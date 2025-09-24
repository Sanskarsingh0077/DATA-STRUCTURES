def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        '''
        dp = [[-1]*(n+1) for _ in range(n+1)]

        def solve(i,j):
            if i >j:
                return 0
            if i == j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j]= 2 + solve(i+1,j-1)
                return dp[i][j]

            dp[i][j]= max(solve(i+1,j),solve(i,j-1))
            return dp[i][j]


        return solve(0,n-1)

        '''

        t = [[0]*(n) for _ in range(n)]

        for i in range(n):
            t[i][i] = 1

        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i + l -1

                if s[i] == s[j]:
                    t[i][j] = 2 + t[i+1][j-1]

                else:
                    t[i][j] = max(t[i][j-1], t[i+1][j])

        return t[0][n-1]