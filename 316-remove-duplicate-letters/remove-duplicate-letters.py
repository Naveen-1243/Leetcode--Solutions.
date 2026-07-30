class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        stack=[]
        seen=set()
        for i in s:
            d[i]-=1
            if i in seen:
                continue
            while stack and i < stack[-1] and d[stack[-1]]>0:
                removed=stack.pop()
                seen.remove(removed)

            stack.append(i)
            seen.add(i)
        return "".join(stack)