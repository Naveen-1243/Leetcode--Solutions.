import heapq
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        count=0
        min_heap=[]
        for first,end in intervals:
            while min_heap and min_heap[0]<first:
                heapq.heappop(min_heap)
            count+=len(min_heap)
            heapq.heappush(min_heap,end)
        return count