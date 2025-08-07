class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        '''
        dp = [[-1]*(n) for _ in range(n)]

        def child1collect(fruits):
            res = 0

            for i in range(n):
                res += fruits[i][i]
                fruits[i][i] = 0
                dp[i][i] = 0

            return res


        def child2collect(i, j,fruits):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
        
            if i == n - 1 and j == n - 1:
                return 0
        
        
        #can't go beyond diagonal or left to diagonal (only have n-1 moves)
            if i == j or i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
        

            bottomLeft = fruits[i][j] + child2collect(i+1,j-1,fruits)
            bottomDown = fruits[i][j] + child2collect(i+1,j,fruits)
            bottomdigonal = fruits[i][j] + child2collect(i+1,j+1,fruits)

            dp[i][j] = max(bottomLeft, bottomDown,bottomdigonal)
            return dp[i][j]



        def child3collect(i,j,fruits):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
        
            if i == n - 1 and j == n - 1:
                return 0
        

            #can't go beyond diagonal or right to diagonal (only have n-1 moves)
            if i == j or j > i:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            topRight = fruits[i][j] + child3collect(i,j+1,fruits)
            topUp = fruits[i][j] + child3collect(i-1,j+1,fruits)
            topdigonal = fruits[i][j] + child3collect(i+1,j+1,fruits)

            dp[i][j]= max(topRight, topUp, topdigonal)
            return dp[i][j]

        
        ans = ((child1collect(fruits))+ (child2collect(0,n-1,fruits))+ (child3collect(n-1,0,fruits)))

        return ans
        '''

        # Bottom Up

        t = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i < j and i + j < n - 1:
                    t[i][j] = 0
                elif i > j and i + j < n - 1:
                    t[i][j] = 0
                else:
                    t[i][j] = fruits[i][j]
                

        #Child 2
        for i in range(1,n):
            for j in range(i+1,n):
                    t[i][j] += max(t[i - 1][j - 1],t[i - 1][j],t[i - 1][j + 1] if j + 1 < n else 0)

        #Child 3
        for j in range(1,n):
            for i in range(j+1,n):
                    t[i][j] += max(
            t[i+1][j-1] if i + 1 < n and j - 1 >= 0 else 0,
            t[i][j-1] if j - 1 >= 0 else 0,
            t[i-1][j-1] if i - 1 >= 0 and j - 1 >= 0 else 0
        )


        child1 = sum(fruits[i][i] for i in range(n))
        child2 = t[n-2][n-1]
        child3 = t[n-1][n-2]

        return child1 + child2 + child3


        

        
        

