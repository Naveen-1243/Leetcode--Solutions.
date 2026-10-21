class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        
        graph=collections.defaultdict(list)
        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))
        
        res=0
        visited=set()

        def dfs(node):
            nonlocal res
            visited.add(node)
            for nei,cost in graph[node]:
                if nei not in visited:
                    res+=cost
                    dfs(nei)
        
        dfs(0)
        return res