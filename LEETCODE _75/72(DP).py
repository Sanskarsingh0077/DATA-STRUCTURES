class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[-1]*(n+1) for _ in range(m+1)]
        
        '''
        def solve(i,j):

            if i == m:
                return n-j #INSERT

            if j == n:
                return m-i #DELETE
            
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j]= solve(i+1,j+1)
                return dp[i][j]
            else:
                insert = 1 + solve(i,j+1)
                delete = 1 + solve(i+1,j)
                replace = 1 + solve(i+1,j+1)

                dp[i][j] = min(insert,delete,replace)
                return dp[i][j]

        return solve(0,0)

        '''
        

        #Right to left filling the dp table : using past values to get the answer.
        def solve(m:int,n:int):
            if m == 0 or n == 0:
                return m+n

            if dp[m][n] != -1:
                return dp[m][n]

            if word1[m-1] == word2[n-1]:
                dp[m][n] = solve(m-1,n-1)
                return dp[m][n]
            
            else:
                insert = 1 + solve(m,n-1)
                delete = 1 + solve(m-1,n)
                replace = 1 + solve(m-1,n-1)
                
                dp[m][n] = min(insert,replace,delete)
                return dp[m][n]

        return solve(m,n)
        
        '''
        #Bottom Up Approach:

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j

                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                else:
                    
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    replace = 1 + dp[i-1][j-1]

                    dp[i][j] = min(insert,delete,replace)

        return dp[m][n]     
        ''' 
             