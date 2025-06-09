class Solution:
    def numTilings(self, n: int) -> int:
        dp=[-1]*(n+1)
        m= 1000000007

        #Bottom Up Tabulation Method
        if n == 0:
            return 0
        if n <= 2:
            return n 
        if n== 3:
            return 5

        dp[1]=1
        dp[2]=2
        dp[3]=5

        for i in range(4,n+1):
            dp[i] = (2*(dp[i-1])+dp[i-3])%m #(Main Formula)%m

        return dp[n]
'''
Trick is in Formula f(n) = [2*f(n-1)] + [f(n-3)] - derive formula creation general equation and subtracting it with f(n-1) :- f(n) - f(n-1)

f(n) = f(n-1)+f(n-2)+2*f(n-3)+......+2*f(0)
f(n-1) = f(f-2)+f(n-3)+ 2*f(n-4) + 2*f(n-5) +......+2*f(0)

f(n)-f(n-1) = f(n-1) + f(n-3)
f(n) = 2*f(n-1) + f(n-3) 
'''

'''
        #Memoization: Top Down Approach

        def solve(n):
            if n== 0:
                return 0
            if n<=2:
                return n

            if n==3:
                return 5

            if dp[n]!= -1:
                return dp[n]

            dp[n] = ((2*solve(n-1)) + solve(n-3))%m
            return dp[n]

        return solve(n)
'''



        
        
        



        
        