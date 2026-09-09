class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        first=1
        second=1
        i=2
        while i<=n:
            res=first+second
            first=second
            second=res
            i+=1
        return res