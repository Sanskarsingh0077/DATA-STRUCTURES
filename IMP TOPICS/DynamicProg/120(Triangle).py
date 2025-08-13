def minimumTotal(self, triangle: List[List[int]]) -> int:  

        n = len(triangle)
        dp = [[None] * len(row) for row in triangle]
        
        def solve(row, col):
            if row == n-1:
                return triangle[row][col]

            if dp[row][col] is not None:
                return dp[row][col] 

            down = solve(row+1,col)
            down_right = solve(row+1, col+1)


            dp[row][col] = triangle[row][col] + min(down, down_right) 

            return dp[row][col]

        return solve(0,0)