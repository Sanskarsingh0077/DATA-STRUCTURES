# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        #Approach 1: Recusrsive DFS 
        '''
        level_values =[]

        def dfs(node,level):
            if node is None:
                return
            
            if level == len(level_values):
                level_values.append(node.val)
            
            else:
                level_values[level] += node.val

            dfs(node.left,level+1)
            dfs(node.right, level+1)

        dfs(root,0)

        result= level_values.index(max(level_values))+1

        return result

        '''
        '''
         Logic:
            1.	Traverse the tree depth-first, going as deep as possible down each path.
            2.	Pass the current level as a parameter in the recursive call.
            3.	Use a list level_sums where each index stores the sum of nodes at that level.
            4.	When visiting a node:
            •	If it’s the first time reaching that level, append its value to the list.
            •	Otherwise, add its value to the existing sum at that level.
            5.	After traversal, find the index of the maximum sum in the list and return index + 1.

        [TC: O(N)- visit each node once]
        [SC: O(N)- due to recursion stack (in worst case) + list of sums.]
        '''

        #Approach 2 : Iterative BFS using Deque 


        queue=deque([root])
        max_sum=float('-inf')
        max_level = 0
        level = 1

        while queue:
            level_size = len(queue)
            level_sum = 0

            for i in range(level_size):
                node=queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum>max_sum:
                max_sum = level_sum
                max_level = level

            level+=1

        return max_level
        '''
        Logic:
            1.	Use a queue to do a level-order traversal (process nodes level by level).
            2.	At each level:
            •	Track the total sum of all nodes at that level.
            •	Enqueue all the children of the current level’s nodes for the next round.
            3.	After processing each level, compare its sum to the current max sum.
            4.	Track the level number that gave the highest sum.

        [TC: O(n)-Each node is visited once.]
        [SC: O(w) - Width of the tree (max number of nodes at any level); worst case = O(n)]
        '''

        