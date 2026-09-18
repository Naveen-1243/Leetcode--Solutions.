class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        max_count=0
        def dfs(i,j):
            nonlocal count,max_count
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 
            else:
                count+=1
                max_count=max(count,max_count)
                grid[i][j]=0
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count=0
                    dfs(i,j)
        return max_count