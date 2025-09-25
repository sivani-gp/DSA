class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        c_profit = 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]<buy_price:
                buy_price = prices[i]
            c_profit = prices[i] - buy_price
            max_profit = max(c_profit,max_profit)
        return max_profit


        