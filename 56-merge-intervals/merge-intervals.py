class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        first=intervals[0][0]
        second=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if second >= start:
                second=max(second, end)
            
            else:
                res.append([first, second])
                first=start
                second=end
        
        res.append([first, second])
        return res