class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index , height = stack.pop()

                maxArea = max(maxArea, height * (i - index))
                start = index
            else:
                stack.append((start,h))

            
        for i , h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

'''

Algorithm ---> O(n):

	1.	Initialize an empty stack to store (start_index, height) and maxArea = 0.
	2.	Traverse the histogram bars from left to right.
	3.	For each bar, pop taller bars from the stack and compute their area using the current index as the right boundary.
	4.	Push the current bar with the earliest start index it can extend to.
	5.	After traversal, compute areas for remaining bars by extending them to the end.
	6.	Return maxArea.


'''