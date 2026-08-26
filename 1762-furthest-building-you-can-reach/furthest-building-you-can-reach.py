import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap=[]
        count=0
        for i in range(len(heights)-1):
            if heights[i] < heights[i+1]:
                diff = abs(heights[i] - heights[i+1])
                heapq.heappush(heap, diff)

                if heap and len(heap) > ladders:
                    smallest = heapq.heappop(heap)
                    bricks -= smallest
                
                    if bricks < 0:
                        return i
        
        return len(heights)-1