class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            
        odd=[]
        res=0
        for k,v in d.items():
            if v%2==0:
                res+=v
            else:
                odd.append(v)
        
        total=0
        for i in odd:
            total += i-1
        
        return res+total+1 if len(odd)>0 else res