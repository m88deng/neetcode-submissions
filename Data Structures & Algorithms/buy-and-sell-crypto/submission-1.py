class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 0

        max_profit = 0
        
        while r < n:
            while l < r and prices[l] > prices[r]:
                l += 1

            buy = prices[l]
            sell = prices[r]

            profit = sell - buy

            if profit > max_profit:
                max_profit = profit
            
            r += 1

        return max_profit