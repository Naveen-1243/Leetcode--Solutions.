class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        start=points[0][0]
        end=points[0][1]
        new=[]
        for i in range(1,len(points)):
            first,second=points[i]

            if end >= first:
                end=min(end,second)
            
            else:
                new.append([start,end])
                start=first
                end=second
        new.append([start,end])

        return len(new)