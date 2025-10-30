class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)

        res = 0
        curr = 0
        prev = 0

        for i in range(n):
            curr = target[i]

            if curr<0 and prev > 0 or curr>0 and prev <0:
                res += abs(curr)

            elif curr > prev:
                res += (curr-prev)

            prev = curr

        return res