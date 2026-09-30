class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        depth=0
        res=[]
        for i in seq:
            if i =="(":
                res.append(depth % 2)
                depth+=1
            else:
                depth-=1
                res.append(depth%2)
        return res