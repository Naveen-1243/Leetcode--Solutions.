class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        prevend=intervals[0][1]
        count=0
        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                count += 1
                prevend = min(prevend, end)
        return count