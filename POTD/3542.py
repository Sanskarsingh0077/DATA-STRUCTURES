class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Brute Force Solution O(n^2)

        '''
        opr = 0
        st = set(nums)
        n = len(nums)

        for target in st:
            if target == 0:
                continue

            flow = False
            for i in range(n):
                if nums[i] == target:
                    if not flow:
                        flow = True
                        opr += 1

                elif nums[i] < target:
                    flow = False

        return opr

        '''

        # Optimal Solution (Monotonic Increasing Stack) O(n)

        n = len(nums)
        stack = []
        opr = 0

        for i in range(n):
            while stack and stack[-1]> nums[i]:
                stack.pop()

            if nums[i] == 0:
                continue
            
            if not stack or stack[-1] < nums[i]:
                opr += 1
                stack.append(nums[i])

        return opr


            





