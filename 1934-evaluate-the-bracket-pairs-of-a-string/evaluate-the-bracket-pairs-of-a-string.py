class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        l=0
        d={}
        for key,val in knowledge:
            d[key]=val
        res=""
        while l<len(s):
            if s[l]=="(":
                l+=1
                x=""
                while s[l]!=")":
                    x+=s[l]
                    l+=1
                if x in d:
                    res += d[x]
                else:
                    res += "?"
                l+=1
            else:
                res += s[l]
                l+=1
        return res