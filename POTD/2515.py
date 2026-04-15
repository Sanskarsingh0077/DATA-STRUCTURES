class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        res = float('inf')
        for i in range(n):
            if words[i] == target:

                straight_dist = abs(i - startIndex)
                circular_dist = n - straight_dist

                res = min(straight_dist, circular_dist , res)

        return res if res != float('inf') else -1
                

