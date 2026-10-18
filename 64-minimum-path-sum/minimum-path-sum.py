from functools import cache
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        @cache
        def dp(i,j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            if i>=m or j>=n:
                return float('inf')
            right=dp(i,j+1)
            left=dp(i+1,j)
            
            return grid[i][j]+min(right,left)

        return dp(0,0)