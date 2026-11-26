class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        d={}
        for i in strs:
            s="".join(sorted(i))
            
            if s in d:
                d[s].append(i)
            else:
                d[s]=[i]
        
        res=[]
        for k,v in d.items():
            res.append(v)
        return res