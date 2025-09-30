class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        n = len(nums)

        # Normal Simulation (O(n^2))
        '''
        while n != 1:
            for i in range(n-1):
                nums[i] = (nums[i] + nums[i+1])%10

            n -= 1

        return nums[0]
        '''

        # Binomial Coefficient(O(n))
        total = 0

        for i in range(n):
            total += math.comb(n-1,i)*nums[i]

        return total % 10