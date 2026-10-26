class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        m=len(grid)
        n=len(grid[0])
        def dfs(r,c):
            
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]==0:
                return 0

            res=grid[r][c]
            grid[r][c]=0

            res+=dfs(r+1,c)
            res+=dfs(r,c+1)
            res+=dfs(r-1,c)
            res+=dfs(r,c-1)

            return res

        count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]!=0:
                    if dfs(r,c)%k == 0:
                        count+=1
        return count