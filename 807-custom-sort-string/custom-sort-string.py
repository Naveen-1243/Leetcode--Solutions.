class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        s1=list(order)
        s2=list(s)
        res=""
        for i in s1:
            for j in s2:
                if i == j:
                    res+=i
            
        for j in s2:
            if j not in s1:
                res+=j
        
        return res