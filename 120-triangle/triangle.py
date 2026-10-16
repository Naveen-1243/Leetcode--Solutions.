from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        @lru_cache(None)
        def dp(i,j):
            if i == n-1:
                return triangle[i][j]
            
            return triangle[i][j] + min(dp(i+1,j),dp(i+1,j+1))
            
            
        return dp(0,0)