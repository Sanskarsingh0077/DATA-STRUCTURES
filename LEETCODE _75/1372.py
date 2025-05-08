# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0
        '''

        def solve(root,steps,goleft):
            if root is None:
                return

            self.maxPath =max(self.maxPath,steps)

            if goleft:
                solve(root.left,steps+1,False)
                solve(root.right, 1,True)
            else:
                solve(root.right,steps+1,True)
                solve(root.left, 1 , False)

        solve(root.left, 1, False)
        solve(root.right, 1, True)

        return self.maxPath
        '''
        '''
        Approach: Classic Recursive DFS with Direction Tracking :

        1.	We use a recursive function solve(root, steps, goleft):
        •	steps: how many steps we’ve taken in the current ZigZag path.
        •	goleft: a boolean that tells us the last direction we moved in.
        •	True: we just moved left, so next move should go right.
        •	False: we just moved right, so next move should go left.
        2.	At every node:
        •	We update the maximum path seen so far using self.maxPath = max(self.maxPath, steps).
        3.	Recursive calls:
        •	If we just went left (goleft == True):
        •	We go left again → restart path → steps = 1, now direction is right.
        •	We go right → continue path → steps + 1, now direction is right (False).
        •	If we just went right (goleft == False):
        •	We go right again → restart path → steps = 1, now direction is left.
        •	We go left → continue path → steps + 1, now direction is left (True).
        4.	Start from root’s left and right:
        •	Try both directions: solve(root.left, 1, False) and solve(root.right, 1, True).

        TC : O(N)
        SC : O(h)

        '''
        
        def solve(root,left,right):
            
            if root is None:
                return

            self.maxPath = max(self.maxPath,left,right)
            solve(root.left,right+1,0)
            solve(root.right,0,left+1)
  

        solve(root,0,0)

        return self.maxPath

        '''
        Approach 2: Symmetrical Recursive DFS with Two Path Counters (left, right):

        We want to find the longest ZigZag path in a binary tree. A ZigZag path means we alternate directions — go      left, then right, then left, and so on.

        Here’s what we do:
        1.	We use a recursive function solve to travel through the tree.
        2.	At every node, we keep track of two things:
        •	How many moves we’ve made going left, then right, then left… (left)
        •	And how many going right, then left, then right… (right)
        3.	Every time we visit a node, we update the maximum ZigZag path length using max(self.maxPath, left, right).
        4.	We move to the left child and increase the right counter (since we just went left).
        5.	We move to the right child and increase the left counter (since we just went right).
        6.	This way, we explore all possible ZigZag paths in the tree and keep track of the longest one.

        TC : O(N)
        SC : O(h)
        '''

            