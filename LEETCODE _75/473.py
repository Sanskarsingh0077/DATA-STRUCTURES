# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.pathSums = defaultdict(int)

        self.pathSums[0] = 1

        def dfs(r , currSum):
            if r is None:
                return
            
            currSum += r.val

            self.paths+= self.pathSums[currSum - targetSum]
            self.pathSums[currSum] += 1

            if r.right:
                dfs(r.right, currSum)
            if r.left:
                dfs(r.left, currSum)

            self.pathSums[currSum] -=1

        dfs(root,0)

        return self.paths

        '''
        O(N) Approach:

    1.	Initialize a dictionary pathSums to store how many times each prefix sum has occurred.
	•	Start with pathSums[0] = 1 to account for the entire path starting from the root.
	2.	Use DFS to traverse the tree.
	•	Keep a currSum (current running prefix sum).
	•	At each node:
	•	Add its value to currSum.
	•	Check if currSum - targetSum exists in pathSums. If yes, add that count to the total valid paths.
	•	Update pathSums[currSum] += 1 (to include current node’s sum).
	•	Recurse into left and right children.
	•	After recursion, backtrack: pathSums[currSum] -= 1 (removes the influence of current node for   other      branches).
	3.	Return total paths counted.

    	•	Time Complexity: O(N)
            You visit each node once.
	    •	Space Complexity: O(H + N)
            H for recursion stack, N for the map in worst case.
        '''
