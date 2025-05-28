class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Using Sorting
        '''
        nums=sorted(nums,reverse = True)
        ans=0

        for i in range(len(nums)):
            if i == k-1:
                ans=nums[i]
        
        return ans

        '''

        #one liner sorting 
        '''

        result = sorted(nums,reverse=True)[k-1]

        return result

        '''

        #Using maxHeap

        import heapq

        max_heap = [-x for x in nums]   # Step 1: Convert to negative for max-heap-O(n)
        heapq.heapify(max_heap)         # Step 2: Turn list into a heap (min-heap of negatives)-O(n)

        for _ in range(k - 1):          # Step 3: Pop k-1 largest elements- O(k log n)
            heapq.heappop(max_heap)
        
        return -heapq.heappop(max_heap)  # Step 4: Return the k-th largest (negated back) - O(log n)


        #   Time Complexity: O(n + k log n)
        #    Space Complexity: O(n)



    

