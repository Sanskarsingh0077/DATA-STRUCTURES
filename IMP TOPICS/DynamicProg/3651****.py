class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        INF = 10**18
        cost = [[INF] * n for _ in range(m)]

        # Store (value, r, c)
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()

        for _ in range(k + 1):
            best = INF
            i = 0
            L = len(cells)

            # ---- TELEPORT PHASE ----
            while i < L:
                val = cells[i][0]
                j = i

                # update best over this value-group
                while j < L and cells[j][0] == val:
                    _, r, c = cells[j]
                    if cost[r][c] < best:
                        best = cost[r][c]
                    j += 1

                # apply best to all in this value-group
                for t in range(i, j):
                    _, r, c = cells[t]
                    cost[r][c] = best

                i = j

            # ---- NORMAL DP PHASE ----
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        cost[i][j] = 0
                    else:
                        if i + 1 < m:
                            cost[i][j] = min(cost[i][j], cost[i + 1][j] + grid[i + 1][j])
                        if j + 1 < n:
                            cost[i][j] = min(cost[i][j], cost[i][j + 1] + grid[i][j + 1])

        return cost[0][0]
    
    '''
        m = len(grid)
        n = len(grid[0])

        cost = [[float('inf')] * (n) for _ in range(m)]

        cells = []
        for i in range(m):
            for j in range(n):
                cells.append([i,j])

        cells.sort(key=lambda x: grid[x[0]][x[1]])

        for step in range(k+1):
            best = float('inf')

            for idx in range(len(cells)):
                r = cells[idx][0]
                c = cells[idx][1]

                best = min(best, cost[r][c])

                if idx + 1 < len(cells) and grid[r][c] == grid[cells[idx+1][0]][cells[idx+1][1]]:
                    continue

                back = idx
                while back >= 0 and grid[cells[back][0]][cells[back][1]] == grid[r][c]:
                    cost[cells[back][0]][cells[back][1]] = best
                    back -= 1
            

            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if i == m-1 and j == n -1:
                        cost[i][j] = 0

                    if i + 1 < m:
                        cost[i][j] = min(cost[i][j], cost[i+1][j]+grid[i+1][j])

                    if j + 1 < n:
                        cost[i][j] = min(cost[i][j], cost[i][j+1]+ grid[i][j+1])


        return cost[0][0]
    '''
    

'''
        dp = [[[-1] * (k+1) for _ in range(n)] for _ in range(m)]
        def solve(i,j,k):
            
            if i >= m or j >= n or k < 0:
                return float('inf')

            if i == m-1 and j == n-1:
               return 0

            if dp[i][j][k] != -1:
                return dp[i][j][k]
            
            # Path 1
            path1 = float('inf')
            if i + 1 < m:
                path1 = grid[i+1][j] + solve(i+1, j, k)

            # Path 2
            path2 = float('inf')
            if j + 1 < n:
                path2 = grid[i][j+1] + solve(i, j+1, k)
            
            #Teleportation
            mini = float('inf')
            for x in range(m):
                for y in range(n):
                    if (x == i and y == j) or grid[x][y] > grid[i][j]:
                        continue
         
                    mini = min(mini, solve(x, y, k-1))

            dp[i][j][k] = min(mini, min(path1,path2))
            return dp[i][j][k]
    
    
        return solve(0, 0 , k)
'''

        
        

        


                


                

                







