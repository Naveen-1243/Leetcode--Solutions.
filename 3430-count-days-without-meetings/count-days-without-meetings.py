class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        first=meetings[0][0]
        second=meetings[0][1]
        count=0
        for i in range(1, len(meetings)):
            start, end = meetings[i]

            if second >= start:
                second = max(second,end)

            else:
                count += second-first + 1
                first=start
                second=end
        
        count += second-first + 1
        return days-count