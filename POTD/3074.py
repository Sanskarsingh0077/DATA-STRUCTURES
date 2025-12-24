class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)

        total = sum(apple)
        res = 0
        i = 0
        while total > 0:
            total -= capacity[i]
            res += 1
            i += 1

        return res
