from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        
        visited=set()
        rec=set()

        def dfs(node):
            if node in rec:
                return True
            if node in visited:
                return False
            visited.add(node)
            rec.add(node)

            for nei in graph[node]:
                if dfs(nei):
                    return True
            rec.remove(node)
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True