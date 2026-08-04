class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        a=min(nums)
        b=max(nums)
        for i in range(a,b+1):
            if i not in nums:
                res.append(i)
        return res