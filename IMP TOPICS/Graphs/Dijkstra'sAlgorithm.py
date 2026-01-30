import heapq
from typing import List, Dict

def shortestPath(n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    # Create Adjacency List
    adj = {}

    for i in range(n):
        adj[i] = []

    # Fill Adjacency List
    for source, des, weight in edges:
        adj[source].append([des, weight])

    print("Adjacency List:", adj)

    #Create map to store final answer
    shortest = {}
    minheap = [[0, src]] # min heap to get shortest distance

    #Filling minheap and map
    while minheap:
        w1, n1 = heapq.heappop(minheap)

        if n1 in shortest:
            continue

        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minheap, [w1 + w2, n2])

    #checking if any node is not still in map fill it
    for i in range(n):
        if i not in shortest:
            shortest[i] = -1


    return shortest

#TC : O( E log V)

# Don't Work for -ve Edges
# Can't Help in detecting -ve cycles

n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
src = 0

print(shortestPath(n,edges,src))