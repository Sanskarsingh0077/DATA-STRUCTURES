class Solution:
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    def possibleReach(self,i, j, mid, visited,n,grid):
        if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or grid[i][j] > mid:
            return False

        visited[i][j] = True

        if i == n-1 and j == n-1:
            return True

        for dir in self.directions:
            i_ = i+dir[0]
            j_ = j+dir[1]

            if self.possibleReach(i_,j_,mid,visited,n,grid):
                return True

        return False

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        l = grid[0][0]
        r = (n*n)-1
        
        result = 0

        while l <= r:
            mid = l + (r-l)//2

            visited = [[False]*(n) for _ in range(n)]

            if self.possibleReach(0,0,mid,visited, n,grid): #DFS or BFS
                result = mid
                r = mid - 1

            else:
                l = mid + 1

        return result