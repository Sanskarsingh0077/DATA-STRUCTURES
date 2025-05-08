# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


#Approach 3: DFS with help of stacks
        '''
Explanation:
	•	stack = [[root, 1]]:
Stack holds pairs of (node, depth) — start with root at depth 1.
	•	res = 1:
Stores the max depth encountered so far.
	•	while stack:
DFS loop; each iteration processes one node.
	•	node, depth = stack.pop():
Pop the top node and its depth.
	•	res = max(res, depth):
Update max depth if the current one is deeper.
	•	stack.append(...):
Push left and right children with incremented depth.
	•	return res:
Final result is the deepest depth found.
'''

        if not root:
            return 0

        stack=[[root,1]]
        res = 1

        while stack:
            node,depth = stack.pop()

            if node:
                res = max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])


        return res


#Approach 1: Recursively go to each node.
'''
    •	if not root:
    Base case: if the node is None, return 0 (no depth to count).
	•	return 1 + max(...):
    Add 1 for the current node and recursively compute the maximum of:
	•	self.maxDepth(root.left) → depth of left subtree
	•	self.maxDepth(root.right) → depth of right subtree

    So this builds depth from bottom up, adding +1 as the recursive calls return.
'''
'''
        if not root:
            return 0
        
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))

'''


#Approach 2: Use Breath first search and keep counting levels using dequeue()

'''
         Explanation:
	    •	deque([root]):
        Initializes a queue for BFS with the root node.
	    •	while q:
        Each loop iteration = one level of the tree.
	    •	for _ in range(len(q)):
        Processes all nodes in the current level (ensures level count is accurate).
	    •	node = q.popleft():
        Gets the next node to process.
	    •	q.append(node.left/right):
        Adds children to the queue for the next level.
	    •	level += 1:
        After finishing one level, increment the depth counter.
	    •	return level:
        After all levels are processed, return the total.


'''
'''
        if not root:
            return 0

        level = 0
        q= deque([root])

        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1

        return level

'''

        




        