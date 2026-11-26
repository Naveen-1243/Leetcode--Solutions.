class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        if n<10:
            return False
        
        x=10
        change=0
        while n:
            if n-x<0:
                break
            n=n-x
            change+=1
            x-=1

        return False if change%2==0 else True