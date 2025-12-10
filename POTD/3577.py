class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(complexity)
        res = 1

        for i in range(1,n):
            if complexity[i] <= complexity[0]:
                return 0

            res = (res * i) % mod

        return res