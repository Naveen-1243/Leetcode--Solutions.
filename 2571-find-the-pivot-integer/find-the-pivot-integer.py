class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        
        total=(n*(n+1))//2
        left=0
        for i in range(1,n+1):
            left+=i
            right=total - left +i
        
            if right==left:
                return i
        return -1