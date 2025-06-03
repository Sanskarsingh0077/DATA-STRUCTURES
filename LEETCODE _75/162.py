class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n-1

        while left< right:
            mid = left + (right-left)//2

            if nums[mid]<nums[mid+1]:
                left = mid +1

            else:
                right = mid
            
        return left

        '''
        Approach:
        - Basic Binary Searching and checking mid and next element

        - Time Complexity: O(logn)
        '''