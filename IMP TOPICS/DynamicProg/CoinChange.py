class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down Memoization
        '''
        dp = [-1] * (amount + 1)

        def dfs(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')

            if dp[rem] != -1:
                return dp[rem]

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + dfs(rem- coin))

            dp[rem] = ans
            return dp[rem]

        res = dfs(amount)

        return res if res != float('inf') else -1

        '''

        #Bottom Up

        minCoin = [float('inf')]*(amount + 1)
        minCoin[0] = 0

        for i in range(1, len(minCoin)): # O(Amount)
            for coin in coins: # O(Coins)
                if coin <= i and minCoin[i-coin] != float('inf'):
                    minCoin[i] = min(minCoin[i], 1 + minCoin[i - coin])

        
        return minCoin[amount] if minCoin[amount] != float('inf') else -1

        # TC : O(amount * coins)







        


        


        
