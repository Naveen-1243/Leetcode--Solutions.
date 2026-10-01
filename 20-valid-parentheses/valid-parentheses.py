class Solution:
    def isValid(self, s: str) -> bool:
        
        d={")":"(","]":"[","}":"{"}
        opened={"(","[","{"}
        stack=[]
        for i in s:
            if i in opened:
                stack.append(i)
            else:
                if stack:
                    if (stack[-1]=="(" and i==")") or (stack[-1]=="[" and i=="]")or(stack[-1]=="{" and i=="}"):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack)==0