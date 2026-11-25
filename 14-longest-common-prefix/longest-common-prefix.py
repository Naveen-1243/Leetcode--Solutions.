class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        s=sorted(strs)
        a=s[0]
        b=s[-1]
        res=""
        for i in range(len(s[0])):
            if a[i]!=b[i]:
                return res
            else:
                res += a[i]
        return res