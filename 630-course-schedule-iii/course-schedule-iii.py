import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])
        heap=[]
        max_time=0
        for time, end_day in courses:
            heapq.heappush(heap, -time)
            max_time += time

            if max_time > end_day:
                popped=-heapq.heappop(heap)
                max_time -= popped
        
        return len(heap)