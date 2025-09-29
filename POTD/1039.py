class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        t = [[-1]*(n+1) for _ in range(n+1)]

        def solve(i,j):
            if j - i + 1 < 3:
                return 0

            if t[i][j] != -1:
                return t[i][j]

            res = float('inf')
            for k in range(i+1,j):

                score = values[i]*values[j]*values[k] + solve(i,k) + solve(k,j)

                res = min(res, score)

            t[i][j]= res
            return t[i][j]


        return solve(0,n-1)