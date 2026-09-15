class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen=set()
        graph=[[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()

        def dfs(node):
            if node==destination:
                return True
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
            return False
        return dfs(source)