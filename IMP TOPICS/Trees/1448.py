# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        stck = [(root, float('-inf'))]

        # Iterative Method

        while stck:
            node, largest = stck.pop()

            if largest <= node.val:
                good += 1

            largest = max(largest, node.val)

            if node.left : stck.append((node.left, largest))
            if node.right : stck.append((node.right, largest))

        return good         

        '''
        # TC : O(n) 
        
        Each node is:
            •	Pushed to the stack once
            •	Popped from the stack once
            •	Constant work per node
            
        # SC :  O(h) - height of tree
         
        '''


        

        

        