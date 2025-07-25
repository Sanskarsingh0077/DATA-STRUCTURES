def maxSum(self, nums: List[int]) -> int:
        setval = set()

        maxsum = 0
        negsum = float('-inf')

        for num in nums:
            if num <= 0:
                negsum = max(negsum, num)

            elif num not in setval:
                    maxsum += num
                    setval.add(num)

        return negsum if maxsum == 0 else maxsum