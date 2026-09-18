from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        empty,fresh,rotten=0,1,2
        total_fresh=0
        time=-1

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    total_fresh+=1
        
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
            
                for ni,nj in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
                    if ni<0 or ni>=m or nj<0 or nj>=n or grid[ni][nj]!=1:
                        continue
                    if grid[ni][nj]==1:
                        total_fresh-=1
                        grid[ni][nj]=2
                        q.append((ni,nj))
            time+=1
        if total_fresh != 0:
            return  -1
        return max(0,time)