class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if profit < 0:
                left = right

            else:
                max_profit = max(max_profit, profit)

            right += 1

        return max_profit