"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}

        if not node:
            return None

        def dfs(curr):
            if curr in mp:
                return mp[curr]

            clone = Node(curr.val)
            mp[curr] = clone

            for n in curr.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)

    # TC:  O( V + E )
