def maxProfit(self, prices: List[int]) -> int:
        n =len(prices)
        m = 2

        '''
        dp = [[-1]*(m)for i in range(n+1)]

        def solve(day,buy):

            if day>= n:
                return 0

            if dp[day][buy] != -1:
                return dp[day][buy]

            if buy: #Buying: True
                take = solve(day + 1, False) - prices[day]  # buy stock
                skip = solve(day + 1, True) # don't buy
                dp[day][buy] = max(take,skip)

            else: #Buying : False
                sell = prices[day] + solve(day + 1, True)  # sell and buy after that
                skip = solve(day + 1, False) # don't sell

                dp[day][buy] = max(sell,skip)

            return dp[day][buy]


        return solve(0,True)
        '''

        #Greedy-DP hybrid 
        
        if n<=1:
            return 0

        cash = 0    # Max profit if you do not hold a stock
        hold = -prices[0]  #Max profit if you do hold a stock
  

        for i in range(1,n):
            cash = max(cash, hold+prices[i])  # Sell the stock at prices[i], pay fee

            hold = max(hold,cash-prices[i]) # Buy the stock at prices[i]

        return cash