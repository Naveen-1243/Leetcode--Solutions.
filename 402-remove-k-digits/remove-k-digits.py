class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==1:
            return "0"
        stack=[]
        for i in num:
            while stack and k>0 and i<stack[-1]:
                stack.pop()
                k-=1
            stack.append(i)
            
        while stack and k>0:
            stack.pop()
            k-=1
            
        x=""
        for i in stack:
            x+=i
        
        res=x.lstrip('0')
        return "0" if res=="" else res
        