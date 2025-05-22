class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #Fast Solution:

        def dfs(adj: List[List[Tuple[int, int]]], visited: List[bool], minChange: List[int], currCity: int) -> None:
            visited[currCity] = True
            for neighbourCity in adj[currCity]:
                if not visited[neighbourCity[0]]:
                    if neighbourCity[1] == 1:
                        minChange[0] += 1
                    dfs(adj, visited, minChange, neighbourCity[0])
    
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], -1))
        visited = [False] * n
        minChange = [0]
        dfs(adj, visited, minChange, 0)
        return minChange[0]

        '''
        #Approach 2: BFS(Iterative)

        adj= {}

        for i in range(n):
            adj[i] = []

        for u,v in connections:
            adj[u].append((v,1))  # 1 → original direction u → v
            adj[v].append((u,0))  # 0 → reverse direction (virtual) v → u

        visited = [False] * n
        res= 0
        queue= [0]
        visited[0] = True

        while queue:
            node = queue.pop(0)
            for neighbour, direction in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    res += direction
                    queue.append(neighbour)

        return res

        '''
        

        '''
        #Approach (DFS-Recursive):

        #Making a Adjacency List with 1 - Original Direction(u->v) and 0 - Virtual Reverse Direction(v->u)
        adj= {}

        for i in range(n):
            adj[i] = []

        for u,v in connections:
            adj[u].append((v,1))  # 1 → original direction u → v
            adj[v].append((u,0))  # 0 → reverse direction (virtual) v → u

        
        #Solving problem by using adjacency list
        visited = [False]* n # visited = [ False , False , False ........n ]
        res = 0

        def dfs(node):
            nonlocal res
            visited[node] = True
            for neighbour, direction in adj[node]:
                if not visited[neighbour]:
                    res+= direction
                    dfs(neighbour)

        dfs(0)

        return res
    '''
    '''
        Approach(DFS):
            1.	Build a graph from the connections:
                •	For each connection u → v, store:
                •	(v, 1) in adj[u] → this is the original direction (may need to reverse).
                •	(u, 0) in adj[v] → virtual reverse direction (for traversal).
            2.	Start DFS from node 0 (because all cities must reach 0).
            3.	During DFS traversal:
                •	Mark the current node as visited.
                •	For each neighbor:
                •	If the edge is in the original direction (1), it means the road goes away from 0, so:
                •	You must reverse this edge → increase the count.
                •	Then, visit that neighbor recursively.
            4.	Repeat for all reachable cities.
            5.	Return the total count of reversed edges.

            Time Complexity = O(n) - You visit each node once → O(n), You process each edge twice (because it’s bidirectional in the adjacency list) → O(2 * (n - 1)) = O(n)
            Space Complexity: O(n) - Adjacency list stores each node and its neighbors → O(n), Visited array → O(n), Recursive call stack in DFS → worst case O(n) deep
    '''

       






    

        
        


        

        