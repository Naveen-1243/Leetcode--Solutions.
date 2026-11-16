class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        N=len(nums)
        max_prod=nums[0]
        min_prod=nums[0]
        res=nums[0]
        def dp(i):
            nonlocal max_prod, min_prod, res
            if i>=N:
                return res
            
            new_max=max(nums[i], max_prod*nums[i], min_prod*nums[i])
            new_min=min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod=new_max
            min_prod=new_min
            res=max(res, new_max, new_min)
            dp(i+1)
        
        dp(1)
        return res