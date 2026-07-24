class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in prices:
            if i < min_price:
                min_price = i
            prof = i - min_price
            if prof > max_profit:
                max_profit = prof
        return max_profit
        