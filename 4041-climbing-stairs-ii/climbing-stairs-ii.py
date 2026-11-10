from functools import cache
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dp(i):
            if i>=n:
                return 0
            ans=float('inf')
            for j in range(1,4):
                if i+j<=n:
                    ans=min(ans, costs[i+j-1] + j*j + dp(i+j))
            return ans
        return dp(0)