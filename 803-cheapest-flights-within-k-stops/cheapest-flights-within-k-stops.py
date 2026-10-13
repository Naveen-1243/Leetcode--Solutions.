from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, total_flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for s,dest,p in total_flights:
            graph[s].append((dest,p))
        
        min_heap=[(0,src,0)]
        d={(src,0):0}
        while min_heap:
            price,node,flights=heapq.heappop(min_heap)

            if node == dst:
                return price
            if flights == k+1:
                continue
            for new_node, new_price in graph[node]:
                total = price+new_price
                state=(new_node, flights+1)
                if total < d.get(state, float('inf')):
                    d[state]=total
                    heapq.heappush(min_heap,(total,new_node,flights+1))
        
        return -1