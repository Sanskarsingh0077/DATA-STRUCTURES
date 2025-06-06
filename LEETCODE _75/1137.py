class Solution:
    def tribonacci(self, n: int) -> int:
        #Top Down Approach DP:
        '''
        dp =[-1]*(n+1) #Memoization : Storing solved values in list so that if needed can be used later.
        def solve(n):
            if n == 0:
                return 0

            if n == 1 or n==2:
                return 1

            if dp[n] != -1:
                return dp[n]
            
            dp[n] = solve(n-1) + solve(n-2)+ solve(n-3)
            return dp[n]
            

        return solve(n)

        # Time : O(n) / Space : O(n)

        '''

        #Bottom - up Approach DP:
        '''
        dp = [-1]*(n+1)

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        #Assign whats Given 
        dp[0]=  0
        dp[1] = 1
        dp[2] = 1

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]

        # Time : O(n) / Space : O(n)

        '''

        #Bottom - up Optimized Space DP(O(n)):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a = 0
        b = 1
        c = 1
        
        for i in range(2,n):
            answer = a + b + c
            a = b
            b = c
            c = answer

        return c

        #	Time: O(n) 	/ Space: O(1) (no array needed)


