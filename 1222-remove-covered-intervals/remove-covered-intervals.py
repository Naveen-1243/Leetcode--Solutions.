class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 1:
            return 1
        intervals.sort(key=lambda x: (x[0], -x[1]))
        start=intervals[0][0]
        end=intervals[0][1]
        res=[]
        for first,second in intervals[1:]:
            if first>=start and second<=end:
                continue
            else:
                res.append([start,end])
                start=first
                end=second
        res.append([start,end])
        return len(res)

        """
        [18533,23127]]
        [46321,59199]

        """