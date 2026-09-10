class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort()

        start=intervals[0][0]
        end=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            first,second=intervals[i]

            if end>=first:
                end=max(end,second)
            else:
                res.append([start,end])
                start=first
                end=second
        res.append([start,end])
        return res