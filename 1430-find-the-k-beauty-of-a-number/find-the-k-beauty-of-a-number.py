class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        output=0
        window=s[:k]
        if num%int(window)==0:
            output+=1
        
        for i in range(k,len(s)):
            window = window[1:] + s[i]

            if int(window)>0 and num%int(window) == 0:
                output+=1
        return output