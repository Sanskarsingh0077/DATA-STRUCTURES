# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Thought of the day:“Helper functions should help. If they’re just extra — skip them.”
        if root is None:
            return
            
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root

        return right if right else left

        return self.lowestCommonAncestor(root,p,q)


        '''
        Approach:
        •	If the root is None, it returns None.
        •	If the root matches either p or q, it returns the root.
        •	It recursively searches for p and q in the left and right subtrees.
        •	If both left and right recursive calls return non-null, the current root is the LCA.
        •	Otherwise, it returns the non-null result from either left or right.

        Time Complexity:
        O(n) — where n is the number of nodes in the binary tree, as each node is visited once.

        '''