class Solution:
    def isValid(self, s: str) -> bool:
        opened={'(','{','['}
        stack=[]
        for i in s:
            if i in opened:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i==")" and stack[-1]=="(" or i=="}" and stack[-1]=="{" or i=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
        
        return len(stack)==0