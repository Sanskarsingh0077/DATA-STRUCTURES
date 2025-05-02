# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #Iterative Approach DFS: 
        '''
        def get_leaves(root):
            leaves= []
            stack=[root]


            if root is None:
                return []

            while stack:
                node = stack.pop()

                if node.left is None and node.right is None:
                    leaves.append(node.val)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

            return leaves

        return get_leaves(root1) == get_leaves(root2)
        '''
        #Recursive Approach: Optimized and clean
        
        def recursiveleaves(root):
            if root is None:
                return []
                
            if root.left is None and root.right is None:
                return [root.val]

            return recursiveleaves(root.left)+ recursiveleaves(root.right)
            
        return recursiveleaves(root1)==recursiveleaves(root2)
        

        

        


