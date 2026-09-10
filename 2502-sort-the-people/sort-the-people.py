class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        
        new_sort = sorted(d.items(), key=lambda x: x[0], reverse=True)
        
        res=[]
        for k, v in new_sort:
            res.append(v)
        return res