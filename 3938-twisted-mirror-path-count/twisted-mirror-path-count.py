class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        mod=10**9 + 7
        @cache
        def dp(i,j,dir):
            if i<0 or i>m-1 or j<0 or j>n-1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            
            if grid[i][j]==0:
                return (dp(i+1,j,1) + dp(i,j+1,0)) % mod
            
            if grid[i][j]==1:
                if dir==0:
                    return dp(i+1,j,1)
                else:
                    return dp(i,j+1,0)
        
        return dp(0,0,0)