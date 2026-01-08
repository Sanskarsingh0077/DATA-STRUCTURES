class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute O(n)
        '''
        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                return i

        return -1

        '''

        # Using Binary Search [ O(log n) ]

        '''

        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid

            # Left Half Sorted

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                
                else:
                    left = mid + 1

            # right Half Sorted
            else:

                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1


        return -1
        '''

        #Better Binary Search

        def binary_Search(left, right):
            idx = -1

            while left <= right:
                mid = left + (right-left)//2

                if nums[mid] == target:
                    idx = mid
                    break
                
                elif nums[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1


            return idx

        def findpivot(n):
            left = 0
            right = len(nums) - 1

            while left < right:
                mid = left + (right - left)//2

                if nums[mid] > nums[right]:
                    left = mid + 1

                else:
                    right = mid

            return right


        pivot = findpivot(len(nums))

        idx = binary_Search(0, pivot -1) # left Half 
        if idx != -1:
            return idx

        idx = binary_Search(pivot, len(nums) - 1) # right Half
        
        return idx


