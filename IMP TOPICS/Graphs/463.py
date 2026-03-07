class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        perimeter = 0

        def dfs(i, j):
            nonlocal perimeter
            if i >= row or j >= col or i < 0 or j < 0 or grid[i][j] == 0:
                perimeter += 1
                return

            if grid[i][j] == -1:
                return 

            grid[i][j] = -1 # Mark Visited

            #Check All Directions
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1, j)
            dfs(i, j-1)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i,j)
                    

        return perimeter