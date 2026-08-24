import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res=[]
        max_heap=[]
        for i in range(k):
            sqr_sum=points[i][0]**2 + points[i][1]**2
            heapq.heappush(max_heap, (-sqr_sum, points[i]))
        
        for i in range(k, len(points)):
            sqr_sum=points[i][0]**2 + points[i][1]**2
            if sqr_sum <= -max_heap[0][0]:
                heapq.heappush(max_heap, (-sqr_sum, points[i]))
                heapq.heappop(max_heap)
        return [item[1] for item in max_heap]