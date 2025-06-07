class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        #Top Down Memoization 
        
        n= len(cost)
        dp = [-1]*n

        def solve(idx,cost):
            if idx>= n:
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            #Two Possible ways 
            a = cost[idx] + solve(idx+1,cost) # 1 Step forward
            b = cost[idx] + solve(idx+2,cost) # 2 Step forward

            dp[idx] = min(a,b)
            return dp[idx]

        return min(solve(0, cost),solve(1, cost))

        #Time Complexity: O(n)
        '''

        #Bottom UP DP

        n = len(cost)

        if n == 2:
            return min(cost[0],cost[1])

        for i in range(2,n):
            cost[i] = cost[i] + min(cost[i-1],cost[i-2]) #Fill the array with previous costs

        return min(cost[n-1],cost[n-2]) #Get the last two costs and check for min. 

        #Time Complexity: O(n) - checking and visiting n elements only once.

