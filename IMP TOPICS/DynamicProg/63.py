class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        '''

        dp = [[-1]*(n) for _ in range(m)]

        def solve(i,j):
            if (i >= m or i < 0 or  j >= n or j < 0) or obstacleGrid[i][j] == 1:
                return 0

            if i == m-1 and j == n-1:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            right = solve(i, j+1)
            left = solve(i+1 , j)

            dp[i][j] = right + left
            return dp[i][j]


        return solve(0,0)

        '''

        t = [[0]*n for _ in range(m)]

        #fill row
        for col in range(n):
            if col >= 1 and grid[0][col-1]:
                t[0][col] = 0

                grid[0][col] = 1

            elif grid[0][col] == 1:
                t[0][col] = 0
            else:
                t[0][col] = 1

        #fill col
        for row in range(m):
            if row > 0 and grid[row-1][0] == 1:
                t[row][0] = 0

                grid[row][0] = 1

            elif grid[row][0] == 1:
                t[row][0]= 0

            else:
                t[row][0] = 1

        for row in range(1,m):
            for col in range(1,n):
                if grid[row][col] == 1:
                    t[row][col] = 0

                else:
                    t[row][col] = t[row-1][col] + t[row][col-1]

        return t[m-1][n-1]





