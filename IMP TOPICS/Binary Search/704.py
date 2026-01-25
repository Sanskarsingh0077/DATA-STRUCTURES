class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0

        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid 
                break

            if nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1 

        return -1