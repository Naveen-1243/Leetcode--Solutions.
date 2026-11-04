from functools import cache
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        total=0

        @cache
        def dp(i,total):
    
            if total == amount:
                return 0
            if i==n:
                return float('inf')
            
            if total>amount:
                return float('inf')
            #take
            take=1 + dp(i,total+coins[i])

            #skip
            skip=dp(i+1,total)

            result=min(take,skip)
            return result

        res=dp(0,0)
        if res == float('inf'):
            return -1
        return res