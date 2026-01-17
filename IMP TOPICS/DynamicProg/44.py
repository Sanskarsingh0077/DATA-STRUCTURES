class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        n = len(s)
        m = len(p)

        dp = [[-1]*(m) for _ in range(n)]

        def solve(i , j):
            #Base Case
            if i < 0 and j < 0:
                return True

            if i>= 0 and j<0:
                return False

            if i < 0 and j >= 0:
                for ptt in range(j+1):
                    if p[ptt] != '*':
                        return False

                
                return True


            if dp[i][j] != -1:
                return dp[i][j]


            #Conditions
            #1 matches
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] =  solve(i-1, j-1)
                return dp[i][j]

            #2 nothing
            if p[j] == '*':
                dp[i][j] = solve(i-1, j) or solve(i, j-1)
                return dp[i][j]

            
            dp[i][j]= False
            return dp[i][j]

    
        return solve(n-1,m-1)

        '''

        #Tabulation : with extra space
    
        n = len(p)
        m = len(s)

        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True
        for j in range(1,m+1):
            dp[0][j] = False

        for i in range(1,n+1):
            flag = True
            for ii in range(1,i+1):
                if p[ii - 1] != '*':

                    flag = False
                    break


            dp[i][0] = flag

        for i in range(1,n+1):
            for j in range(1,m+1):
                #Conditions
                #1 matches
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] =  dp[i-1][j-1]

                #2 nothing
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                else:
                    dp[i][j]= False
        
        
        return dp[n][m]



