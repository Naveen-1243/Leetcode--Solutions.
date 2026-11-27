class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first sort
        #check 1stand 2nd if both can be merged then merge

        intervals.sort()
        res=[]
        start=intervals[0][0]
        end=intervals[0][1]

        for x in intervals[1:]:
            first,second=x
            
            if first<=end:
                end=max(end,second)
            else:
                res.append([start,end])
                start=first
                end=second
        res.append([start,end])
        return res