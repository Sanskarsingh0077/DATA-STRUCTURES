"""

Floyd–Warshall Algorithm
------------------------
Purpose:
    Compute shortest paths between ALL pairs of nodes in a graph.

Key Idea:
    Try every node as an intermediate ("via") and relax all (i, j) paths.

Time Complexity:
    O(V^3)

Space Complexity:
    O(V^2)

Common Use Cases:
    - All-pairs shortest path
    - Character conversion problems
    - Detecting negative cycles
"""


from typing import List


class Solution:
    def floydWarshall(self, dist: List[List[int]]) -> None:
        """
        Modifies the input matrix in-place so that dist[i][j]
        becomes the shortest distance from i to j.

        GFG Convention:
            -1 represents no direct edge
        """

        n = len(dist)
        INF = 10**9

        # STEP 1: Normalize input
        # Convert -1 (no edge) → INF
        # Distance from node to itself = 0
        for i in range(n):
            for j in range(n):
                if dist[i][j] == -1:
                    dist[i][j] = INF
                if i == j:
                    dist[i][j] = 0

        # STEP 2: Floyd–Warshall core logic
        # Try every node as an intermediate (via)
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    # Relax path only if both segments exist
                    if dist[i][via] < INF and dist[via][j] < INF:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][via] + dist[via][j]
                        )

        # STEP 3: Convert INF back to -1
        for i in range(n):
            for j in range(n):
                if dist[i][j] == INF:
                    dist[i][j] = -1


"""
====================================================
INTERVIEW QUESTION VERSION (LeetCode-style)
====================================================

Problem:
--------
You are given two strings source and target of the same length.
You can convert characters using given transformations.
Each transformation has a cost.

Find the minimum cost to convert source → target.
Return -1 if impossible.

Approach:
---------
- Treat characters as graph nodes (a–z → 0–25)
- Build adjacency matrix
- Run Floyd–Warshall
- Sum character-wise conversion costs
"""


class CharacterConversion:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:

        INF = float('inf')

        # 26 letters → adjacency matrix
        dist = [[INF] * 26 for _ in range(26)]

        # Distance to self = 0
        for i in range(26):
            dist[i][i] = 0

        # Build graph edges
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        # Floyd–Warshall
        for via in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][via] < INF and dist[via][j] < INF:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][via] + dist[via][j]
                        )

        # Calculate total cost
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue

            u = ord(s) - ord('a')
            v = ord(t) - ord('a')

            if dist[u][v] == INF:
                return -1

            total_cost += dist[u][v]

        return total_cost


# Example usage
if __name__ == "__main__":
    solver = CharacterConversion()
    print(
        solver.minimumCost(
            source="abcd",
            target="acbe",
            original=["a", "b", "c", "c", "e", "d"],
            changed=["b", "c", "b", "e", "b", "e"],
            cost=[2, 5, 5, 1, 2, 20]
        )
    )