class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0

        right_sum= sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

#Approach:

# Initialize left_sum to 0 (nothing on the left initially)
# Initialize right_sum as the total sum of the array

# Loop through the array:
#   - Subtract current element from right_sum (exclude it from the right side)
#   - If left_sum equals right_sum → current index is the pivot, return it
#   - Add current element to left_sum (include it in left side for next iteration)

# If no pivot index found, return -1