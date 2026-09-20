class Solution:
    def reverseDegree(self, s: str) -> int:
        
        res=0
        for i,ch in enumerate(s):
            res += (i+1) * (26-(ord(ch) - ord('a')))
        return res