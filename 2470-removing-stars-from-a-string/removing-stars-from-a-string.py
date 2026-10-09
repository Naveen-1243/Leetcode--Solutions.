class Solution:
    def removeStars(self, s: str) -> str:
        
        stack=[]
        for i in s:
            if i =="*":
                if not stack:
                    return ""
                else:
                    stack.pop()
            else:
                stack.append(i)
        return "".join(stack)