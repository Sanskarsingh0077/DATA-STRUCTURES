#House Robber O(1) - Solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Constant Space O(1) 
        def helper(houses):
            prev = 0
            prevprev = 0

            for money in houses:
                take = money + prevprev
                skip = prev

                curr = max(take,skip)

                prevprev = prev
                prev = curr

            return prev

        return helper(nums)