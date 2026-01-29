# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        # While Root is True
        while curr:
            if p.val > curr.val and q.val > curr.val: # If P and Q > Root.val ---> Search Right
                curr = curr.right

            elif p.val < curr.val and q.val < curr.val: # If P,Q < Root ---> Search Left
                curr = curr.left

            else:
                return curr # If Split return curr
            

        #TC : O(H) --> H being the height of tree