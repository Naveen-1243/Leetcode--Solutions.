from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        @lru_cache(None)
        def path(i,j):
            
            if i>=m or j>=n:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            
            return path(i+1,j) + path(i,j+1)
        
        return path(0,0)