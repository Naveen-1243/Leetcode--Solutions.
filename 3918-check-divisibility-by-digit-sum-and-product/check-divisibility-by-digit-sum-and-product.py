class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        sum1=0
        pro=1
        for i in str(n):
            sum1 += int(i)
            pro *= int(i)
        
        return n%(sum1 + pro) == 0