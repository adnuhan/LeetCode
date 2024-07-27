class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        output = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                output = max(prices[sell] - prices[buy], output)
            else:
                buy = sell
            sell += 1

        return output
