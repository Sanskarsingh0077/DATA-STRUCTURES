class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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


