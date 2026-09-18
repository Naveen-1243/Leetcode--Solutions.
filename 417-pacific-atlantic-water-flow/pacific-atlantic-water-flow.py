from collections import deque
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m,n=len(heights),len(heights[0])
        p_q=deque()
        p_seen=set()
        a_q=deque()
        a_seen=set()

        for j in range(n):
            p_q.append((0,j))
            p_seen.add((0,j))
        
        for i in range(1,m):
            p_q.append((i,0))
            p_seen.add((i,0))
        
        for i in range(m):
            a_q.append((i,n-1))
            a_seen.add((i,n-1))
        
        for j in range(n):
            a_q.append((m-1,j))
            a_seen.add((m-1,j))
        
        def bfs(q,seen):
            while q:
                i,j=q.popleft()
                
                for ni,nj in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
                    if ni<0 or ni>=m or nj<0 or nj>=n:
                        continue
                    if (ni,nj) in seen:
                        continue
                    if heights[ni][nj]<heights[i][j]:
                        continue
                    q.append((ni,nj))
                    seen.add((ni,nj))
        bfs(p_q,p_seen)
        bfs(a_q,a_seen)
        return list(p_seen.intersection(a_seen))