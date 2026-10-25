class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        sym="*+-/"
        for i in tokens:
            if i not in sym:
                stack.append(int(i))
            else:
            
                first=stack.pop()
                second=stack.pop()
                if i == "+":
                    stack.append(first + second)
                elif i == "*":
                    stack.append(first * second)
                elif i == "-":
                    stack.append(second-first)
                elif i == "/":
                    stack.append(int(second / first))
            
        return stack[-1]