class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        '''
        res = 0

        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    res = max(res, j-i)

            
        return res
        '''

        # Optimized

        n = len(colors)
        
        ans = 0
        
        for i in range(n):
            if colors[i] != colors[0]:
                ans = max(ans, i)
            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)
        
        return ans
