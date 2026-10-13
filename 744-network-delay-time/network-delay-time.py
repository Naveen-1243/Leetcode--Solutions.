import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        
        graph=defaultdict(list)
        for u,v,time in times:
            graph[u].append((v,time))
        
        d={k:0}
        min_heap=[(0,k)]

        while min_heap:
            dist,node = heapq.heappop(min_heap)
            if dist>d[node]:
                continue
            for nei,t in graph[node]:
                new_dist = dist+t

                if nei not in d or new_dist < d[nei]:
                    d[nei] = new_dist
                    heapq.heappush(min_heap, (new_dist, nei))
        
        if len(d) != n:
            return -1
        return max(d.values())
        
        