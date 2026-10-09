class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m,n=len(isConnected),len(isConnected[0])
        visited=[False] * m

        def dfs(i):
            visited[i]=True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        count=0
        for i in range(m):
            if not visited[i]:
                dfs(i)
                count += 1
            
        return count