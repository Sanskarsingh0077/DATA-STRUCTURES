class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        countEven = 0
        countOdd = 0
        

        for num in nums:
            if num %2 == 0:
                countEven += 1

            else:
                countOdd += 1

        parity = nums[0]%2
        alternating = 1

        for i in range(n):
            currParity = nums[i] % 2

            if currParity != parity:
                alternating += 1
                parity = currParity


        return max(countEven, countOdd, alternating)