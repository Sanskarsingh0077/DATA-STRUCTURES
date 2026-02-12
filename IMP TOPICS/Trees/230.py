# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stck = []
        curr = root

        while curr or stck:
            while curr:
                stck.append(curr)
                curr = curr.left

            curr = stck.pop()
            n += 1 

            if n == k:
                return curr.val

            curr = curr.right