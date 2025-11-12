class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        count1 = nums.count(1)

        if count1:
            return n - count1

        opr = float('inf')

        for i in range(n):
            GCD = nums[i]
            for j in range(i+1,n):
                GCD = math.gcd(GCD, nums[j])

                if GCD == 1:
                    opr = min(opr, j-i)

                    break


        if opr == float('inf'):
            return -1

        return opr + (n-1)

