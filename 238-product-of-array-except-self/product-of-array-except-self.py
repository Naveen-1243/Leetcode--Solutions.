class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        N=len(nums)
        if nums.count(0)>1:
            return [0]*N
        total=1
        for i in nums:
            if i != 0:
                total *= i
        
        res=[]
        change=False
        if nums.count(0)==1:
            change=True
        for i in nums:
            if not change:
                res.append(total//i)
            else:
                if i ==0:
                    res.append(total)
                else:
                    res.append(0)
        return res