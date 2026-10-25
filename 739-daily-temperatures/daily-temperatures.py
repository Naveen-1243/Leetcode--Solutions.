class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i,v in enumerate(temperatures):
            while stack and v>stack[-1][1]:
                ii,vv=stack.pop()
                res[ii]=i-ii
            
            stack.append((i,v))
        return res
            

            