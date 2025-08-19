class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)

        dp = [[-1]*(n+1) for _ in range(m+1)]
        '''
        #Memoization DP:
        def solve(i,j):
            if i >= m or j >= n:
                return 0

            if text1[i] == text2[j]: #both math then increase i and j both
                return 1 + solve(i+1,j+1)

            if dp[i][j] != -1: #Memoization
                return dp[i][j]

            else:
                include_text1 = solve(i,j+1) #Take i and increase j
                include_text2 = solve(i+1,j) #Take j and increase i
                dp[i][j]= max(include_text1,include_text2) 
                return dp[i][j]

        return solve(0,0)

        #Time Complextiy: (m+1) * (n+1) => O(m*n)

        '''


        #Bottom Up Tabulation:

        
        #Filling First Row Zero
        for row in range(m+1):
            dp[row][0] = 0

        #Filling First Col Zero 
        for col in range(n+1):
            dp[0][col] = 0

        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max((dp[i][j-1]),(dp[i-1][j]))
        
        # Printing the Longest Common Subsequence
        i = m
        j = n
        res = []
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                res.append(text1[i-1])
                i -= 1
                j -= 1

            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i-=1
                else:
                    j -= 1

        res.reverse()

        print("".join(res))


        return dp[m][n]