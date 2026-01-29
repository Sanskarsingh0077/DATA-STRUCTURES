# I traverse the main tree, and for each node, I verify whether the subtree rooted at that node matches subRoot exactly in structure and values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self,r, s):
        if not r and not s:
            return True

        if r and s and r.val == s.val:
            return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right)

        return False


