class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()


        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbour in rooms[node]:
                dfs(neighbour)

        dfs(0)

        return len(visited) == len(rooms)

        #“For every room I can unlock from here, go visit that room too.”

        '''
        Approach: Using Recursion DFS

        	1.	Initialize a visited set.
            2.	Define a recursive DFS function:
                •	If a room is already visited, return.
                •	Otherwise, add it to visited and call DFS on all the rooms whose keys are in the current room.
            3.	Start DFS from room 0.
            4.	After traversal, check if len(visited) == total_rooms.

        
        '''