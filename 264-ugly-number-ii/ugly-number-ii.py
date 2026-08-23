import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        heap=[1]
        seen={1}
        for i in range(n):
            popped = heapq.heappop(heap)
            for x in [2,3,5]:
                product = x * popped

                if product not in seen:
                    seen.add(product)
                    heapq.heappush(heap, product)
        
        return popped