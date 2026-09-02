class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price=prices[0]
        max_profit = 0
        for i in prices[1:]:
            if i < min_price:
                min_price=i
            profit = i - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit