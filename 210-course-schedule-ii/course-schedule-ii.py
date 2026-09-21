class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res=[]
        graph=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            graph[u].append(v)
        path=[0]*numCourses
        def dfs(i):
            if path[i]==1:
                return False
            elif path[i]==2:
                return True
            path[i]=1
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            path[i]=2
            res.append(i)
            return True
        
        for x in range(numCourses):
            if not dfs(x):
                return []
        return res