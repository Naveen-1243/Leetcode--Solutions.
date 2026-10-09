class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        freq=[]
        for k,v in d.items():
            freq.append(v)
        
        s=set(freq)
        return len(s)==len(freq)