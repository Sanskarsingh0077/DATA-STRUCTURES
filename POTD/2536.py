class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Difference Array Technique

        dat = [[0]*n for _ in range(n)]

        # Query to matrix and difference array making
        for query in queries: # O(query * n)
            r1 = query[0]
            c1 = query[1]

            r2 = query[2]
            c2 = query[3]

            for i in range(r1,r2+1):
                dat[i][c1] += 1

                if c2+1 < n:
                    dat[i][c2+1] -= 1

        # Cumulative Sum Calculation
        for i in range(n): # O(n*n)
            for j in range(1,n):
                dat[i][j] += dat[i][j-1]

        return dat

        # TC : O((query* n) + (n * n)) ~ O(n*n)
        # SC : O(1)

            