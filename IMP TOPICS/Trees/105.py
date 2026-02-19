# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base Case Check
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # Root is always preorder first element
        mid = inorder.index(preorder[0]) # get index of root in Inorder

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) # Recursively do left
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]) # Right

        return root

