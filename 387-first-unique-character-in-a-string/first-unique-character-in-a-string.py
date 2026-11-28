class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        org=[] #empty  l e t c o d
        dup=set() #empty e 
        N=len(s)
        for i in range(N):
            if s[i] in org:
                dup.add(s[i])
            else:
                org.append(s[i])

    
        for i in range(N):
            if s[i] not in dup:
                return i
        return -1