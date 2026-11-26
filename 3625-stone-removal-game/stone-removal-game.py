class Solution:
    def canAliceWin(self, n: int) -> bool:
    
        x=10
        if n<10:
            return False
        
        change=0
        while n:
            if n<x:
                break
            n=n-x
            x-=1
            change += 1

        return True if change%2!=0 else False

