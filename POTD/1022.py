# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Iterative
        if not root:
            return 0


        stack = [(root, 0)]
        total = 0

        while stack:
            node, curr = stack.pop()

            curr = curr * 2 + node.val

            if not node.right and not node.left:
                total += curr

            if node.left:
                stack.append((node.left, curr))

            if node.right:
                stack.append((node.right, curr))

        return total
        

        # Recursive DFS:
        '''

        def dfs(node, curr):
            if not node:
                return 0

            curr = curr * 2 + node.val


            if not node.right and not node.left:
                return curr

            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)

        '''