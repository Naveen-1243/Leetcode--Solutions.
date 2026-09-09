class Solution:
    def countCommas(self, n: int) -> int:
        total=0
        start=1000
        comma=1
        while start <= n:
            end = start*1000 -1

            if n<=end:
                total += (n-start+1)*comma
            else:
                total += (end-start+1)*comma
            
            comma += 1
            start *= 1000
        
        return total