class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        symbols="+-*/"
        for i in tokens:
            if stack and i in symbols:
                x=stack.pop()
                x=int(x)
                y=stack.pop()
                y=int(y)
                if i=="+":
                    stack.append(y+x)
                if i=="-":
                    stack.append(y-x)
                if i=="*":
                    stack.append(y*x)
                if i=="/":
                    stack.append(int(y/x))
            else:
                stack.append(int(i))
        return stack[0]