# 994. Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize queue with rotten oranges and count fresh ones
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0  # No fresh orange to rot

        minutes = 0

        # BFS traversal
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
            minutes += 1

        return minutes - 1 if fresh == 0 else -1


        '''
        Approach:

        Step 1: Initialize
            •	Loop through the grid.
            •	Count all fresh oranges.
            •	Add the positions of all rotten oranges to a queue (to perform BFS).

        Step 2: Perform BFS
            •	While the queue is not empty:
            •	Process all rotten oranges in the current queue (current minute).
            •	For each, check 4 directions (up/down/left/right).
            •	If a neighbor is a fresh orange (1), rot it (2) and add it to the queue.
            •	Decrease the fresh count.
            •	After each level, increment the minutes counter.

        Step 3: Return the Result
            •	If fresh == 0, return minutes - 1 (because the last increment is extra after the final rot).
            •	If fresh > 0, return -1 (some fresh oranges were unreachable).
        
        	•	Time: O(n × m)
	        •	Space: O(n × m) – worst-case for the queue
        '''


        

        
        

