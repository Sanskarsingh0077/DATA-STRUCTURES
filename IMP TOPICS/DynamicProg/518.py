class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Top Down Memoization

        '''
        n = len(coins)

        dp = [[-1]*(amount+1) for _ in range(n)]

        def solve(index, amount):
            if amount == 0: # Found 
                return 1

            if index >= n: # Out Of Bounds
                return 0

            if dp[index][amount] != -1: # Memoize
                return dp[index][amount]


            if coins[index] > amount: # Not Possible
                return solve(index + 1, amount)

            
            take = solve(index, amount - coins[index])
            skip = solve(index + 1, amount)

            dp[index][amount] =  take + skip 

            return dp[index][amount]

        return solve(0, amount)

        '''
        n = len(coins)
        dp = [[0]* (amount + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        
        for i in range(n):
            for a in range(1, amount + 1):
                # Skip
                if i > 0:
                    dp[i][a] = dp[i-1][a]

                # Take 
                if coins[i] <= a:
                    dp[i][a] += dp[i][a-coins[i]]
        
        return dp[n-1][amount]




        

