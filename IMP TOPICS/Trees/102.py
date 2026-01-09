# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def solve(node,level):
            if node is None:
                return 

            if level == len(res):
                res.append([])

            res[level].append(node.val)

            left = solve(node.left, level + 1)
            right = solve(node.right, level + 1)

        solve(root, 0)

        return res