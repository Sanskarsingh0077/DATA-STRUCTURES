class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        mod = 10 ** 9 + 7
        '''

        dp = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def solve(rw,cl, currsum):
            if rw >= m or cl >= n:
                return 0

            if rw == m-1 and cl == n-1:
                return 1 if (currsum + grid[m-1][n-1])%k == 0 else 0

            if dp[rw][cl][currsum] != -1:
                return dp[rw][cl][currsum]


            right = solve(rw,cl+1, (currsum + grid[rw][cl])%k)
            down =  solve(rw+1,cl, (currsum + grid[rw][cl])%k)


            dp[rw][cl][currsum] = (down + right) % mod
            return dp[rw][cl][currsum]


        return solve(0,0,0)

        '''

        # Bottom Up 

        t = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        for remain in range(k):
            t[m-1][n-1][remain] = 1 if (remain + grid[m-1][n-1])%k == 0 else 0


        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                for remain in range(k):
                    if i == m-1 and j == n-1:
                        continue

                    R = (remain + grid[i][j]) % k
                    
                    down = t[i+1][j][R]
                    right = t[i][j+1][R]

                    t[i][j][remain] = (down + right) % mod

        
        return t[0][0][0]









            
