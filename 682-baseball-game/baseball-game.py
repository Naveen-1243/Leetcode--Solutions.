class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        if len(stack)==0:
            return 0
        return sum(stack)