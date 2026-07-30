class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        d={}
        res=[]
        count=1
        for i in range(len(nums)):
            if nums[i] == x:
                d[count]=i
                count+=1
        
        for q in queries:
            if q in d:
                res.append(d[q])
            else:
                res.append(-1)
        return res