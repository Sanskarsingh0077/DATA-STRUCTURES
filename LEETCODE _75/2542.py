class Solution:
    import heapq
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2,nums1),reverse = True)

        min_heap = []
        sum_nums1 = 0
        result = 0


        for num2,num1 in pairs:
            heapq.heappush(min_heap,num1)
            sum_nums1 += num1


            if len(min_heap)> k:
                sum_nums1 -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                result = max(result,sum_nums1* num2)

        return result

        #Approach

        '''	
        1.	Sort the pairs in descending order of num2:
            •	Why? Because we want to consider the current num2 as the minimum in the product sum(num1s) × min(num2) — by iterating from highest to lowest num2, we simulate the situation where each num2 acts as the smallest in a selected group.
        2.	Use a min-heap to keep track of the top k largest num1 values:
            •	Because we want the maximum possible sum of num1 values for k pairs.
            •	The heap ensures we always keep the best k values seen so far.
        3.	Iterate over the sorted pairs:
            •	Add each num1 to a min-heap and keep track of their sum (sum_nums1).
            •	If the heap grows beyond size k, remove the smallest num1 (least contributing to sum).
            •	When the heap has exactly k elements:
            •	Calculate the score: sum_nums1 × current num2 (acting as the minimum num2 in selection).
            •	Update the result if this score is greater than the previous max.
        4.	Return the maximum result found.

        •	Time Complexity: O(n log n)
        •	Space Complexity: O(k)

        '''

