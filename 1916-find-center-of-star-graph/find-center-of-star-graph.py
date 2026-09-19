class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        x=0
        y=0
        for k,v in graph.items():
            if len(v)>x:
                x=len(v)
                y=k
        return y