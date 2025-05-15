class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        provinces = 0

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                provinces += 1

        return provinces


        '''
        Approach: DFS to Count Number of Provinces
            1.	Model the problem as a graph:
                •	Each city is a node.
                •	isConnected[i][j] == 1 means there’s an edge between city i and city j.
            2.	Use DFS to find connected components (provinces):
                •	Maintain a visited list to track which cities have already been explored.
            3.	Iterate over all cities:
                •	If a city has not been visited, it starts a new province.
                •	Call DFS from that city to visit all cities in the same province.
                •	Increment the province count.
            4.	DFS explores all connected cities recursively, marking them as visited.
            5.	Return the total count of provinces after processing all cities.
            
        Time Complexity : In total, each cell isConnected[i][j] is checked at most once → overall O(n²)
        Space Complexity : Inside dfs(city), you iterate through all neighbors (each row in the matrix): O(n)
        '''

