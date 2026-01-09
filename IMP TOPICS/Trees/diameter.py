# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(arr) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root

class Solution:
    
    def diameter(self, root : Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.diameter = max(self.diameter, left+ right)
            
            return 1 + max(left, right)
        
        dfs(root)
        
        return self.diameter

arr = [1,2,3,4,5]
root = buildTree(arr)

sol = Solution()

print(sol.diameter(root))