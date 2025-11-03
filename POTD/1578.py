# Greedy

class Solution:
    def minCost(self, s: str, neededTime: List[int]) -> int:
        time = 0
        n = len(s)

        prevMax = 0

        for i in range(n):
            if i>0 and s[i] != s[i-1]:
                prevMax = 0
            

            curr = neededTime[i]
            time += min(prevMax, curr)

            prevMax = max(prevMax, curr)

        return time
