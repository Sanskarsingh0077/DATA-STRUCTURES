class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        '''
        dp = [[-1]*n for _ in range(n)]
        memo = [[-1] * n for _ in range(n)]

        def isPalindrome(idx1,idx2):
            if idx1 >= idx2:
                return True

            if memo[idx1][idx2] != -1:
                return memo[idx1][idx2]

            if s[idx1] != s[idx2]:
                memo[idx1][idx2] = False
                return memo[idx1][idx2]

            memo[idx1][idx2]= isPalindrome(idx1+1, idx2-1)
            return memo[idx1][idx2]

            
        # Recursion + Memoization
        def solve(i,j):
            if dp[i][j] != -1:
                return dp[i][j]


            if isPalindrome(i,j):
                dp[i][j] = 0
                return 0

            res = float('inf')

            for k in range(i,j):
                if isPalindrome(i,k):

                    temp = 1 + solve(k+1,j)

                    res = min(temp, res)

            dp[i][j] = res

            return dp[i][j]

        return solve(0,n-1)
        '''

        # Bottom Up

        n = len(s)
        t = [[False] *n for _ in range(n)]
        
        #Blue Print For filling start
        #Diagonal Elements
        for i in range(n):
            t[i][i] = True

        # for L >= 2

        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i+l-1

                if l == 2:
                    t[i][j] = (s[i] == s[j])

                else:
                    t[i][j] = (s[i]==s[j] and t[i+1][j-1])

        #Blue Print For filling end

        dp = [0]*(n) #dp[i] = min cuts till i

        for i in range(n):
            if t[0][i]:
                dp[i] = 0 # No cuts req

            else:
                dp[i] = float('inf')

                for k in range(i):
                    if t[k+1][i] and 1 + dp[k] < dp[i]:
                        dp[i] = 1 + dp[k]

        return dp[n-1]


