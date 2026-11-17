class Solution:
    def countSubstrings(self, s: str) -> int:
        N=len(s)
        count=0
        for i in range(N):
            for j in range(i+1):
                if s[j:i+1]==s[j:i+1][::-1]:
                    count+=1
        
        return count