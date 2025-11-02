class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        def markGuarded(row, col, matrix):
            #up
            for i in range(row-1,-1,-1):
                if grid[i][col] == 2 or grid[i][col] == 3:
                    break
                grid[i][col] = 1

            #down
            for i in range(row+1,m):
                if grid[i][col] ==2 or grid[i][col] == 3:
                    break
                grid[i][col] = 1

            #left
            for i in range(col-1,-1,-1):
                if grid[row][i] ==2 or grid[row][i] == 3:
                    break
                grid[row][i] = 1

            #right
            for i in range(col+1, n):
                if grid[row][i] == 2 or grid[row][i] == 3:
                    break

                grid[row][i] = 1

        
        grid = [[0]*(n) for _ in range(m)]

        # Mark Guard Positions
        for vec in guards:
            i = vec[0]
            j = vec[1]

            grid[i][j] = 2 #Guard

        
        # Mark Walls Positions:
        for wall in walls:
            i = wall[0]
            j = wall[1]

            grid[i][j] = 3 # Wall

        for guard in guards:
            i = guard[0]
            j = guard[1]

            markGuarded(i,j, grid) #Check Directions and mark

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1

        return count