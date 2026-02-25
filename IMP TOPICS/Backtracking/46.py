class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)

            perms = new_perms

        return perms
        '''

        # Recursive

        used = [False] * len(nums)
        path = []
        res = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return res