# Bellman - Ford Algorithm

# Shortest path from Source to all vertices in Graph.

# Works for -ve Edges
# Helps in detecting -ve cycles
# Works on Directed Graph
# Relax all the vertices v - 1 times

#TC : O(v * e) 


class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        inf = 10**8
        dist = [inf]*V
        
        # Set Src to 0
        dist[src] = 0
        
        # Relax all the vertices v - 1 times
        
        for v in range(1, V):
            for u, v , w in edges:
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u]+w
    
                    
        # Check for Negative Cycle
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                return [-1]
                
                
        return dist
    
print("Bellman - Ford Shortest Path: ",Solution().bellmanFord(V = 5, edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], src = 0))

    


