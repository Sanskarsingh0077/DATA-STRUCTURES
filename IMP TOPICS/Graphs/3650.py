class Solution:
    # Dijkstra Variant
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        # Create a new list of edges with original and reversed edges
        final = []

        for u ,v, w in edges:
            final.append([u,v,w])
            final.append([v,u, 2*w])


        # Populate adj list as per Dijikstra
        adj = [[] for _ in range(n)]

        for u,v,w in final:
            adj[u].append((v,w))

        shortest = {}
        heap = [(0, 0)] # Start From Cost 0 and node 0


        # Pop and push until adj has element
        while heap:
            cost , n1 = heapq.heappop(heap)

            if n1 in shortest:
                continue

            shortest[n1] = cost

            for n2, c2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, (cost + c2 , n2) )


        return shortest[n-1] if n - 1 in shortest else -1 # Return shortest Route