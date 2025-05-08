# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(node): #Helper function for minimum val successor
            while node.left:
                node = node.left
            return node

        #Base Condition:
        if root is None:
            return

        #Search key in left and right subtree recursively
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        
        elif root.val< key:
            root.right = self.deleteNode(root.right,key)
        
        # Node to delete found
        else:
            # When a node has one child:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left


            # Node with two children
            curr= getMin(root.right)
            root.val = curr.val

            root.right =self.deleteNode(root.right, root.val)


        return root

        


'''

        Step-by-Step Approach: Deleting a Node in BST

            1. Search for the node to delete
            •	Start at the root.
            •	If the key is less than the current node’s value, search in the left subtree.
            •	If the key is greater, search in the right subtree.
            •	If the key matches the current node’s value, this is the node you want to delete.

            2. Handle the three cases based on the node’s children

            Case 1: Node has no children (leaf node)
                •	Just remove the node by returning None to its parent.

            Case 2: Node has only one child
                •	Return that one child to the parent. This means you’re bypassing the current node.

            Case 3: Node has two children
                •	You need to preserve the BST structure, so:
                •	Find the inorder successor (smallest node in the right subtree).
                •	Copy its value into the current node.
                •	Now recursively delete the inorder successor (which will fall into case 1 or 2).

            3. Return the updated root
                •	Whether you modified the left or right child, make sure to reassign it properly and return the root after processing.
                
        
         Space Complexity = O(H) due to recursion
         Time Complexity = O(H) = O(log N) (average case), O(N) (worst case)


'''