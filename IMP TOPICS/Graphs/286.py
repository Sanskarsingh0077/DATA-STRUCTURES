class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m  = len(grid)
        n  = len(grid[0])
        visit = set()
        queue = deque()

        def addRoom(i, j):
            if i < 0 or i >= m or j >= n or j < 0 or (i,j) in visit or grid[i][j] == -1:
                return 

            visit.add((i,j))
            queue.append([i,j])


        for i in range(m): #For each row col if it is a gate start
            for j in range(n):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    queue.append([i,j])

        dist = 0
        while queue:
            for i in range(len(queue)):
                r , c = queue.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r,c+1)
                addRoom(r,c-1)

            dist += 1


        
        




