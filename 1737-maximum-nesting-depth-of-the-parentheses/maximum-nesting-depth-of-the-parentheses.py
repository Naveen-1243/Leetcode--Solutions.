class Solution:
    def maxDepth(self, s: str) -> int:
        
        max_c=0
        c=0

        for i in s:
            if i =="(":
                c+=1
                max_c=max(c,max_c)
            elif i ==")":
                c-=1
        return max_c