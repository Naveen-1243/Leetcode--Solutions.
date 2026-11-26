class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini=prices[0]
        best=0

        for i in prices[1:]:
            if i <mini:
                mini=i
            res=i-mini
            best=max(best, res)
        
        return best