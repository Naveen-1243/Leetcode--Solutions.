import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng=[]
        for eff, spd in zip(efficiency, speed):
            eng.append([eff, spd])
        
        eng.sort(reverse=True)
        res=0
        speed_sum=0
        min_heap=[]
        for eff, spd in eng:

            speed_sum += spd
            heapq.heappush(min_heap, spd)
        
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            
            res=max(res, speed_sum * eff)
        return res % (10**9 +7)