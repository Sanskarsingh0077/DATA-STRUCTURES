# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        new=[]

        def dfs(root, level):
            if root is None:
                return
            
            if level == len(new):
                new.append(root.val)

            dfs(root.right,level+1)
            dfs(root.left,level+1)
            

        dfs(root,0)
        return new

        '''
        Approach 1(Recursive):

        This approach performs a Depth-First Search (DFS) traversal of the binary tree to find the rightmost value at each level of the tree.
        •	A list new is initialized to store the rightmost node values for each level.
        •	The dfs function is called recursively on the right and left subtrees.
        •	For each level, if the level index in new is not filled, it appends the current node’s value to new     (this ensures only the first node at each level gets added).
        •	The tree is traversed from right to left (dfs(root.right, level+1) followed by dfs(root.left, level+1)), ensuring that the rightmost nodes are added first.

        TC: O(n) — where n is the number of nodes in the binary tree. Each node is visited once during the DFS traversal.
        SC: O(h) - max needs to go to the depth of tree
        
        Approach 2: Iterative using deque TC: O(n) and SC: O(n)
        '''
        