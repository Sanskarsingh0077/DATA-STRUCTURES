#from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        
        # Initialize BFS queue with entrance and 0 steps
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        
        # Mark entrance as visited so we don't go back
        maze[entrance[0]][entrance[1]] = '+'
        
        # Directions: down, up, right, left
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            row, col, steps = queue.popleft()
            
            # Try all 4 directions
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                # Check bounds and if it's an open path
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.':
                    # If it's on the border and not entrance => exit found
                    if new_row == 0 or new_row == rows - 1 or new_col == 0 or new_col == cols - 1:
                        return steps + 1
                    
                    # Mark as visited and add to queue with +1 step
                    maze[new_row][new_col] = '+'
                    queue.append((new_row, new_col, steps + 1))
        
        # No exit found
        return -1


        '''
        Approach:

        	1.	Initialize the BFS queue with the entrance and step count 0.
            2.	Mark the entrance as visited ("+") to avoid revisiting.
            3.	Use BFS to explore the maze in all directions (up, down, left, right).
            4.	If you reach an open cell '.' on the border, return steps + 1 — it’s the shortest path.
            5.	If all reachable paths are explored and no exit is found, return -1.
            
        Time complexity: O(N * M)
        Space complexity: O(N * M) (queue + visited)


        '''