class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def bfs(starts, visit):
            queue = deque(starts)
            
            for (i,j) in starts:
                visit.add((i,j))
                

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx,ny) not in visit:
                        visit.add((nx,ny))
                        queue.append((nx, ny))
                        
        pacific_starts = [(0,c) for c in range(n)] + [(r,0) for r in range(m)]
        bfs(pacific_starts, pacific)
        
        atlantic_starts = [(r,n-1) for r in range(m)] + [(m-1, c) for c in range(n)]
        bfs(atlantic_starts, atlantic)
        
        res = []
        
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
                    
        return res
        
        

        
        
'''
        row = len(heights)
        col = len(heights[0])


        pacific = set()
        atlantic = set()

        # dfs Function to go all directions
        def dfs(i, j, visit, prevheight):
            if (i, j) in visit or i >= row or j >= col or i < 0 or j < 0 or  heights[i][j] < prevheight:
                return 

            visit.add((i,j))
            dfs(i+1, j, visit, heights[i][j])
            dfs(i-1, j, visit, heights[i][j])
            dfs(i, j+1, visit, heights[i][j])
            dfs(i, j-1, visit, heights[i][j])


        # For Pacific Ocean Cells( Top Row, Left Col)

        for r in range(row):
            dfs(r, 0, pacific, heights[r][0])

        for c in range(col):
            dfs(0, c, pacific, heights[0][c])

        
        # For Atlantic Ocean(Right Col, Bottom row)

        for r in range(row):
            dfs(r, col-1, atlantic, heights[r][col-1])

        for c in range(col):
            dfs(row - 1, c, atlantic, heights[row-1][c])

        # Check if i , j in both sets 
        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])


        return res
'''