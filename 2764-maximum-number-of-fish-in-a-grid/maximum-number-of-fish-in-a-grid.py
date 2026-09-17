class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        count=0
        max_count=0
        def dfs(i,j):
            nonlocal count,max_count
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 
            else:
                count += grid[i][j]
                grid[i][j]=0
                max_count=max(max_count,count)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    count=0
                    dfs(i,j)
        return max_count