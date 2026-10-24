class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def divide(x):
            mm,dd=map(int, x.split("-"))
        
            return sum(months[:mm-1]) + dd
        
        a1=divide(arriveAlice)
        a2=divide(leaveAlice)
        b1=divide(arriveBob)
        b2=divide(leaveBob)

        start=max(a1,b1)
        end=min(a2,b2)

        return max(end-start+1, 0)