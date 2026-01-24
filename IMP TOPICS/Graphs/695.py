class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        '''
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0

            grid[i][j] = -1

            return (1 + dfs(i, j+1) + dfs(i+1, j) + dfs(i,j-1) + dfs(i-1, j))

        '''

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))

            grid[i][j] = -1
            area = 1

            while queue:
                x , y = queue.popleft()

                for dx,dy in directions:
                    nx , ny = x + dx , y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        queue.append((nx, ny))
                        area += 1

            return area


        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:

                    area = bfs(i,j)
                    max_area = max(max_area, area)

        return max_area