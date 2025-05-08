# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)

        '''
        Approach:

        - Basic DFS approach
        - Check root val for val if found return root 
        - Then do recursion on left if root.val > val else right tree recusion

        Time Complexity:  O(h) → h = height of tree
        Space Complexity: O(h) → due to recursion stack

        '''
        

