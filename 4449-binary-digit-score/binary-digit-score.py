class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        
        s1=bin(a)[2:]
        c1=s1.count('1')
        s2=bin(b)[2:]
        c2=s2.count('1')

        if c1>=c2:
            return c1*c2
        return c2//c1