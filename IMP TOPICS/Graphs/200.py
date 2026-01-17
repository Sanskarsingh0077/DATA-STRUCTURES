class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        def bfs(i, j ):
            queue = deque()
            queue.append((i,j))

            grid[i][j] = '$' #visited

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx , y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '$'
                        queue.append((nx, ny))

        '''

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return

            grid[i][j] = '$'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i, j + 1)
            dfs(i , j -1)

        '''


        island = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    island += 1

        return island
    
    
    #TC : O(m * n) 
    #SC : O(m * n)