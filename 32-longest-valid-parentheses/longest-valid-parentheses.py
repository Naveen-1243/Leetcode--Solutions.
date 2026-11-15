class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        best=0
        start=-1
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)

            else:
                if len(stack)==0:
                    start=i
                else:
                    stack.pop()
                    if len(stack)==0:
                        res=i-start
                    else:
                        res=i-stack[-1]
                    best=max(best, res)
        return best