class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        s=sorted(map(str, strs))
        N=len(s[0])
        res=""
        for i in range(N):
            if s[0][i]==s[-1][i]:
                res += s[0][i]
            else:
                break
        return res