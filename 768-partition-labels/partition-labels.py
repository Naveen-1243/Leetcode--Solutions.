class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i, v in enumerate(s):
            d[v]=i

        size=0
        end=0
        res=[]
        for i, v in enumerate(s):
            size += 1
            end=max(end, d[v])
            if i==end:
                res.append(size)
                size=0
        return res