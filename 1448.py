# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(root,check):
            if root.val >= check:
                self.good +=1
            if root.left :
                dfs(root.left,max(check,root.val))
            if root.right :
                dfs(root.right, max(check,root.val))

        dfs(root,root.val)
        return self.good

        #Time Complexity: O(N) — where N is the number of nodes (we visit every node once).
	•	#Space Complexity: O(H) — recursive call stack depth (H = tree height).
        '''
        Approach:

        	•	Initializes a counter to store the number of good nodes.
            •	dfs is a recursive function that explores the tree.
	        •	root is the current node.
	        •	check is the maximum value seen so far from root to the current node.
            •	If the current node’s value is greater than or equal to all ancestors’ values, it’s a good node, so we increment the counter.
            •	We recursively visit left and right children.
	        •	We update check with the max of check and root.val because that becomes the new “barrier” for good nodes further down the path.
            •	We start the DFS from the root node, and the maximum seen so far is the root’s value itself.
            •	We start the DFS from the root node, and the maximum seen so far is the root’s value itself.
        '''
        

            
        