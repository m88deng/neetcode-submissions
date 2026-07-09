class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start, end = 0, 1

        while end < len(prices):
            profit = max(profit, prices[end] - prices[start])
            if prices[end] < prices[start]: # e.g. 10, 1
                start += 1
            else:
                end += 1
        
        return profit