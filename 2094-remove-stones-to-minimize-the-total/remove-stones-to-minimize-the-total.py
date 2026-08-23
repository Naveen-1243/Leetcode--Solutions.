import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        for i in piles:
            heapq.heappush(heap, -i)
        
        while k>0:
            popped=heapq.heappop(heap)
            stones=-popped
            stones=(stones+1)//2
            heapq.heappush(heap, -stones)
            k-=1
        
        return sum(-x for x in heap)