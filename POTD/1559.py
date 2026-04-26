class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        drxns = [(1,0),(-1,0),(0,-1),(0,1)]

        def cycledetectDFS(i, j , prev_i, prev_j):
            if visited[i][j]:
                return True

            visited[i][j] = True

            for d in drxns:
                new_i = i + d[0]
                new_j = j + d[1]

                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == grid[i][j]:
                    if new_i == prev_i and new_j == prev_j:
                        continue

                    
                    if cycledetectDFS(new_i, new_j, i, j):
                        return True

            return False


        visited = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and cycledetectDFS(i,j, i, j):
                    return True

        
        return False
