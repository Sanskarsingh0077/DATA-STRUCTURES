import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        # fill adj with empty list
        for i in range(1, n+1): # 1- indexed and n included
            adj[i] = []

        
        for src, des, time in times:
            adj[src].append((des, time))

        
        shortest = {} # Map to store shortest time from one node to other

        heap = [(0 , k)]

        #Basic Dijsktra for shortest path
        while heap:
            start_time , start_node = heapq.heappop(heap)

            if start_node in shortest:
                continue

            shortest[start_node] = start_time

            for neigh_node , new_time in adj[start_node]:
                if neigh_node not in shortest:
                    heapq.heappush(heap, (start_time + new_time, neigh_node))

            

        #Check if all nodes are visited 

        if len(shortest) != n:
            return -1

        return max(shortest.values())

        #Time Complexity: O(E log V) , where E - Edges V - vertices(nodes)
        #Space Complexity: O(V + E)
