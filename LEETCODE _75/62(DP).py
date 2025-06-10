class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #DP Top-Down Memoization 

        dp = [[-1] * (n + 1) for _ in range(m + 1)] #memoization array 2D
        
        '''
        def solve(i,j,m,n):
            if i == m-1 and j == n-1:
                return 1

            if i<0 or j<0 or i>=m or j>=n:
                return 0

            if dp[i][j] != -1: #Memoization
                return dp[i][j]
            
            right = solve(i , j+1, m, n) #Right Move
            down = solve(i+1 , j, m, n) #Down Move 

            dp[i][j]= right + down #Give all possible ways from going down and right
            return dp[i][j]


        return solve(0,0,m,n)

        '''


        #Bottom Up Tabular DP:

        dp[0][0]= 1

        if m == 1 and n == 1:
            return 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

            
        return abs(dp[m-1][n-1]) #use abs() as used -1 in initialization.



