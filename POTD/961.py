class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)

        '''
        Time : O(N) Space: O(N)

        numset = set()

        for i in range(n):
            if nums[i] not in numset:
                numset.add(nums[i])

            else:
                return nums[i]

        '''

        # Time: O(n) Space: O(1)

        for i in range(n-2):
            if nums[i] == nums[i+1] or nums[i] == nums[i+2]:
                return nums[i]

        return nums[-1]

        
